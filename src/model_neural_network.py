import pandas as pd

# Load the dataset
df = pd.read_csv('data/fraud.csv.bz2')

# Parse the time column as datetime
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

df_cleaned = df.dropna()

X = df_cleaned.drop('fraud', axis=1)
y = df_cleaned['fraud']

# encode categorical variables
from sklearn.preprocessing import OneHotEncoder

# add hour of day as a feature
X['hour'] = X['time'].dt.hour

# Fit OneHotEncoders on training data
enc_product = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
enc_gender = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
enc_state = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
enc_hour = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Fit and transform - reshape needed because OneHotEncoder expects 2D input
product_encoded = enc_product.fit_transform(X[['product_category']])
gender_encoded = enc_gender.fit_transform(X[['gender']])
state_encoded = enc_state.fit_transform(X[['address_state']])
hour_encoded = enc_hour.fit_transform(X[['hour']])

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
print(X.info())

# neural network
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=[10,10], learning_rate = "adaptive", tol=1e-6, max_iter=800, verbose=True)
model.fit(X, y)

import pickle

# Save the model and encoders
with open('model/nn-model.pkl', 'wb') as f:
    pickle.dump({
        'model': model,
        'enc_product': enc_product,
        'enc_hour': enc_hour,
        'enc_gender': enc_gender,
        'enc_state': enc_state,
        'product_cols': product_cols,
        'hour_cols': hour_cols,
        'gender_cols': gender_cols,
        'state_cols': state_cols,
        'model_version': '0.1'
    }, f)

print("Model and encoders saved successfully!")