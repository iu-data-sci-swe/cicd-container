"""Fraud Detection Prediction API Module"""
import pickle
from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger

import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins":
                                 ["localhost", "127.0.0.1",
                                  "http://localhost:*",
                                  "http://127.0.0.1:*"]}})

swagger = Swagger(app)

# Load the model and encoders
with open('model/model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    model = model_data['model']
    enc_product = model_data['enc_product']
    enc_hour = model_data['enc_hour']
    enc_gender = model_data['enc_gender']
    enc_state = model_data['enc_state']
    product_cols = model_data['product_cols']
    hour_cols = model_data['hour_cols']
    gender_cols = model_data['gender_cols']
    state_cols = model_data['state_cols']
    model_version = model_data.get('model_version', 'unknown')

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
        if False: # full model input
            input_df = pd.concat([product_df, gender_df, state_df, hour_df,
                                  pd.DataFrame({
                                      'amount': [amount],
                                      'credit_score': [credit_score]
                                  })], axis=1)

        else:
          # same model as used in training
          input_df = pd.concat([hour_df, product_df, gender_df,
                              pd.DataFrame({
                                  'amount': [amount],
                              })], axis=1)
    except Exception as e:
        raise ValueError(f"could not create input dataframe: {str(e)}") from e

    return input_df

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
              description: Version of the model"""
    return {"model_version": model_version}, 200


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
    if model_version != '0.2':
        return jsonify({"error": f"Model version mismatch: expected 0.1, got {model_version}"}), 500

    try:
        data = request.get_json()
        if not data:
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
            return jsonify({"error": "Missing required fields"}), 400

        try:
            input_df = create_input_dataframe(amount, product_category, time_str, address_state, gender, credit_score)
        except ValueError as e:
            return jsonify({"error": f"Data preparation failed: {str(e)}"}), 400

        try:
            prediction = run_model(input_df)
        except Exception as e:
            return jsonify({"error": f"prediction failed: {str(e)}"}), 500

        return jsonify({"fraud_probability": min(1.0, max(0.0, prediction))}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
