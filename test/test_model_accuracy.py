import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import f1_score, precision_score, recall_score

class TestModelAccuracy:
    """Test for model accuracy"""

    def test_model_accuracy(self):
        """Test that the model accuracy is as expected."""
    
        # Load the dataset
        df = pd.read_csv('data/fraud.csv.bz2')
        # Parse the time column as datetime
        df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

        df_cleaned = df.dropna().copy()

        X = df_cleaned.drop('fraud', axis=1)
        y = df_cleaned['fraud']

        # TODO stratify?
        # hard code random state for reproducibility (test later)
        _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=566571358)

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

        X = X_test.copy()
        y = y_test.copy()

        # add hour of day as a feature
        X['hour'] = X['time'].dt.hour

        # Transform using loaded encoders
        product_encoded = enc_product.transform(X[['product_category']])
        gender_encoded = enc_gender.transform(X[['gender']])
        state_encoded = enc_state.transform(X[['address_state']])
        hour_encoded = enc_hour.transform(X[['hour']])

        # Get feature names for the encoded columns
        product_cols = enc_product.get_feature_names_out(['product_category'])
        gender_cols = enc_gender.get_feature_names_out(['gender'])
        state_cols = enc_state.get_feature_names_out(['address_state'])
        hour_cols = enc_hour.get_feature_names_out(['hour'])

        # Create DataFrames from encoded arrays
        product_df = pd.DataFrame(product_encoded, columns=product_cols, index=X.index)
        gender_df = pd.DataFrame(gender_encoded, columns=gender_cols, index=X.index)
        state_df = pd.DataFrame(state_encoded, columns=state_cols, index=X.index)
        hour_df = pd.DataFrame(hour_encoded, columns=hour_cols, index=X.index)

        # Drop original columns and concatenate encoded ones
        X = X.drop(['product_category', 'gender', 'address_state', 'time'], axis=1)
        # X = pd.concat([X, product_df, gender_df, state_df], axis=1) # everything
        X = pd.concat([hour_df, product_df, gender_df, X["amount"].to_frame()], axis=1) # only hour, product_category, amount

        # Get predictions on validation data
        y_pred = model.predict(X)

        print(pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predicted']))

        # Calculate metrics
        recall = recall_score(y, y_pred)
        precision = precision_score(y, y_pred)
        f1 = f1_score(y, y_pred)

        assert f1 >= 0.1, f"F1 score {f1:.4f} is below expected threshold of 0.1"
        assert recall >= 0.6, f"Recall score {recall:.4f} is below expected threshold of 0.6"
        assert precision >= 0.02, f"Precision score {precision:.4f} is below expected threshold of 0.02"
        

