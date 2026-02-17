"""Fraud Detection Prediction API Module"""
import os
import pickle
from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY

import pandas as pd
import numpy as np
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import tempfile

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins":
                                 ["localhost", "127.0.0.1",
                                  "http://localhost:*",
                                  "http://127.0.0.1:*"]}})

swagger = Swagger(app)

# Prometheus metrics
prediction_counter = Counter('fraud_predictions_total', 'Total number of fraud predictions', ['status'])
prediction_latency = Histogram('fraud_prediction_duration_seconds', 'Duration of fraud predictions in seconds')
prediction_errors = Counter('fraud_prediction_errors_total', 'Total number of prediction errors', ['error_type'])
model_version_gauge = Gauge('model_version_info', 'Model version information', ['version'])

# Get MLflow configuration from environment
mlflow_uri = os.environ.get('MLFLOW_URI', 'http://localhost:5050')
model_name = os.environ.get('MODEL_NAME', 'default_model')

# Set up MLflow
mlflow.set_tracking_uri(mlflow_uri)

# Load the model from MLflow registry
model_uri = f"models:/{model_name}"
model = mlflow.sklearn.load_model(model_uri)

# Get the run_id from the model version
client = MlflowClient(tracking_uri=mlflow_uri)
model_version = client.get_latest_versions(model_name)[0]
run_id = model_version.run_id

# Download encoders artifact from MLflow
with tempfile.TemporaryDirectory() as temp_dir:
    client.download_artifacts(run_id, "encoders", temp_dir)
    encoders_file = os.path.join(temp_dir, "encoders", "encoders.pkl")
    with open(encoders_file, 'rb') as f:
        encoders_data = pickle.load(f)
        enc_product = encoders_data['enc_product']
        enc_hour = encoders_data['enc_hour']
        enc_gender = encoders_data['enc_gender']
        enc_state = encoders_data['enc_state']
        product_cols = encoders_data['product_cols']
        hour_cols = encoders_data['hour_cols']
        gender_cols = encoders_data['gender_cols']
        state_cols = encoders_data['state_cols']
        model_version_str = encoders_data.get('model_version', 'unknown')
        train_date = encoders_data.get('train_date', 'unknown')

# Set model version metric
model_version_gauge.labels(version=model_version_str).set(1)

git_commit = os.environ.get('GIT_COMMIT', 'unknown')

def run_model(input_df):
    """
    Run the fraud prediction model on the input DataFrame.
    """
    prediction = model.predict_proba(input_df)[0][1]
    return prediction


def create_input_dataframe(amount, product_category, time_str, address_state, gender, credit_score):
    """
    Create input DataFrame for the model from the input data.
    """
    # Encode product_category
    try:
        product_category_encoded = enc_product.transform(np.array([product_category]).reshape(1, -1))[0]
    except ValueError as e:
        raise ValueError(f"Unknown product category: {product_category}: {str(e)}") from e

    # Encode gender
    try:
        gender_encoded = enc_gender.transform(np.array([gender]).reshape(1, -1))[0]
    except ValueError as e:
        raise ValueError(f"Unknown gender: {gender}: {str(e)}") from e

    # Encode state
    try:
        state_encoded = enc_state.transform(np.array([address_state]).reshape(1, -1))[0]
    except ValueError as e:
        raise ValueError(f"Unknown state: {address_state}: {str(e)}") from e

    # Extract hour from time
    try:
        dt = datetime.fromisoformat(time_str)
        hour = dt.hour
        hour_encoded = enc_hour.transform(np.array([hour]).reshape(1, -1))[0]
    except Exception as e:
        raise ValueError(f"Invalid time format: {time_str}: {str(e)}") from e

    # Create input DataFrame
    try:
        product_df = pd.DataFrame(product_category_encoded.reshape(1, -1), columns=product_cols, index=[0])
        gender_df = pd.DataFrame(gender_encoded.reshape(1, -1), columns=gender_cols, index=[0])
        state_df = pd.DataFrame(state_encoded.reshape(1, -1), columns=state_cols, index=[0])
        hour_df = pd.DataFrame(hour_encoded.reshape(1, -1), columns=hour_cols, index=[0])
    except Exception as e:
        raise ValueError(f"could not get create data frames: {str(e)}: shape: {product_category_encoded.shape}") from e

    try:
        input_df = pd.concat([product_df, gender_df, state_df, hour_df,
                              pd.DataFrame({
                                  'amount': [amount],
                                  'credit_score': [credit_score]
                              })], axis=1)
    except Exception as e:
        raise ValueError(f"could not create input dataframe: {str(e)}") from e

    return input_df

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    ---
    responses:
      200:
        description: Service is healthy
        schema:
          type: object
          properties:
            status:
              type: string
              description: Health status
            timestamp:
              type: string
              description: Current timestamp
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "model_version": model_version_str
    }), 200


@app.route('/metrics', methods=['GET'])
def metrics():
    """
    Prometheus metrics endpoint.
    ---
    responses:
      200:
        description: Prometheus metrics
    """
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/api/v1/model_version', methods=['GET'])
def get_model_version():
    """return the model version as stored in the model file
    ---
    responses:
      200:
        description: Model version
        schema:
          type: object
          properties:
            model_version:
              type: string
              description: Version of the model
            git_hash:
              type: string
              description: Git commit hash of the model
            train_date:
              type: string
              description: Training date of the model
    """
    return {"model_name": model_name,
            "mlflow_uri": mlflow_uri,
            "model_version": model_version_str,
            "git_hash": git_commit,
            "train_date": str(train_date)
            }, 200


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    """
    Predict fraud probability for a transaction.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            amount:
              type: number
              description: Transaction amount
            product_category:
              type: string
              description: Category of the product
            time:
              type: string
              description: Transaction timestamp
            address_state:
              type: string
              description: State of the transaction address
            gender:
              type: string
              description: Gender of the customer
            credit_score:
              type: integer
              description: Customer's credit score
          required:
            - amount
            - product_category
            - time
            - address_state
            - gender
            - credit_score
    responses:
      200:
        description: Successful prediction
        schema:
          type: object
          properties:
            fraud_probability:
              type: number
              description: Probability of fraud (0.0 to 1.0)
      400:
        description: Missing or invalid JSON data
      500:
        description: Internal server error
    """
    if model_version_str != '0.1':
        prediction_errors.labels(error_type='bad_model_version').inc()
        return jsonify({"error": f"Model version mismatch: expected 0.1, got {model_version_str}"}), 500

    try:
        with prediction_latency.time():
            data = request.get_json()
            if not data:
                prediction_errors.labels(error_type='no_json').inc()
                return jsonify({"error": "No JSON data provided"}), 400

            # Extract fields
            amount = data.get('amount')
            product_category = data.get('product_category')
            time_str = data.get('time')
            address_state = data.get('address_state')
            gender = data.get('gender')
            credit_score = data.get('credit_score')

            if (amount is None
                or product_category is None
                or gender is None
                or credit_score is None
                or time_str is None
                or address_state is None):
                prediction_errors.labels(error_type='missing_fields').inc()
                return jsonify({"error": "Missing required fields"}), 400

            try:
                input_df = create_input_dataframe(amount, product_category, time_str, address_state, gender, credit_score)
            except ValueError as e:
                prediction_errors.labels(error_type='data_preparation').inc()
                return jsonify({"error": f"Data preparation failed: {str(e)}"}), 400

            try:
                prediction = run_model(input_df)
            except Exception as e:
                prediction_errors.labels(error_type='model_inference').inc()
                return jsonify({"error": f"prediction failed: {str(e)}"}), 500

            prediction_counter.labels(status='success').inc()
            return jsonify({"fraud_probability": min(1.0, max(0.0, prediction))}), 200

    except Exception as e:
        prediction_errors.labels(error_type='unknown').inc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8081))
    host = os.environ.get('HOST', '127.0.0.1')
    app.run(host=host, port=port, debug=True)
