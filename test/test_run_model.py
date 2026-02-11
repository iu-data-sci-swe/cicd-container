"""Test cases for the run_model function from fraud_prediction.py"""
import pytest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from fraud_prediction import run_model


class TestRunModel:
    """Test suite for the run_model function"""

    @patch('fraud_prediction.model')
    def test_run_model_returns_probability(self, mock_model):
        """Test that run_model returns the fraud probability from the model"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.3, 0.7]])
        input_df = pd.DataFrame({
            'amount': [100.0],
            'feature1': [1],
            'feature2': [0]
        })

        # Act
        result = run_model(input_df)

        # Assert
        assert result == 0.7
        mock_model.predict_proba.assert_called_once_with(input_df)

    @patch('fraud_prediction.model')
    def test_run_model_with_low_fraud_probability(self, mock_model):
        """Test run_model with a low fraud probability"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.95, 0.05]])
        input_df = pd.DataFrame({
            'amount': [50.0],
            'feature1': [0],
            'feature2': [1]
        })

        # Act
        result = run_model(input_df)

        # Assert
        assert result == 0.05
        assert 0.0 <= result <= 1.0

    @patch('fraud_prediction.model')
    def test_run_model_with_high_fraud_probability(self, mock_model):
        """Test run_model with a high fraud probability"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.1, 0.9]])
        input_df = pd.DataFrame({
            'amount': [5000.0],
            'feature1': [1],
            'feature2': [1]
        })

        # Act
        result = run_model(input_df)

        # Assert
        assert result == 0.9
        assert 0.0 <= result <= 1.0

    @patch('fraud_prediction.model')
    def test_run_model_with_zero_probability(self, mock_model):
        """Test run_model when model predicts zero fraud probability"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[1.0, 0.0]])
        input_df = pd.DataFrame({
            'amount': [10.0],
            'feature1': [0]
        })

        # Act
        result = run_model(input_df)

        # Assert
        assert result == 0.0

    @patch('fraud_prediction.model')
    def test_run_model_with_one_probability(self, mock_model):
        """Test run_model when model predicts 100% fraud probability"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.0, 1.0]])
        input_df = pd.DataFrame({
            'amount': [10000.0],
            'feature1': [1]
        })

        # Act
        result = run_model(input_df)

        # Assert
        assert result == 1.0

    @patch('fraud_prediction.model')
    def test_run_model_extracts_correct_index(self, mock_model):
        """Test that run_model extracts the probability from index [0][1]"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.25, 0.75]])
        input_df = pd.DataFrame({'col1': [1]})

        # Act
        result = run_model(input_df)

        # Assert
        # Should extract [0][1], not [0][0]
        assert result == 0.75
        assert result != 0.25

    @patch('fraud_prediction.model')
    def test_run_model_with_multiple_features(self, mock_model):
        """Test run_model with a DataFrame containing multiple features"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.4, 0.6]])
        input_df = pd.DataFrame({
            'amount': [250.0],
            'credit_score': [700],
            'hour_0': [1],
            'hour_1': [0],
            'product_cat_1': [0],
            'product_cat_2': [1],
            'gender_M': [1],
            'gender_F': [0]
        })

        # Act
        result = run_model(input_df)

        # Assert
        assert result == 0.6
        mock_model.predict_proba.assert_called_once()

    @patch('fraud_prediction.model')
    def test_run_model_with_decimal_probability(self, mock_model):
        """Test run_model returns precise decimal values"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.123456, 0.876544]])
        input_df = pd.DataFrame({'feature': [1]})

        # Act
        result = run_model(input_df)

        # Assert
        assert result == 0.876544
        assert isinstance(result, (float, np.floating))

    @patch('fraud_prediction.model')
    def test_run_model_calls_predict_proba_once(self, mock_model):
        """Test that run_model calls predict_proba exactly once"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.5, 0.5]])
        input_df = pd.DataFrame({'col': [1]})

        # Act
        run_model(input_df)

        # Assert
        assert mock_model.predict_proba.call_count == 1

    @patch('fraud_prediction.model')
    def test_run_model_passes_dataframe_to_model(self, mock_model):
        """Test that run_model passes the input DataFrame to the model"""
        # Arrange
        mock_model.predict_proba.return_value = np.array([[0.3, 0.7]])
        input_df = pd.DataFrame({
            'amount': [100.0],
            'score': [500]
        })

        # Act
        run_model(input_df)

        # Assert
        called_with = mock_model.predict_proba.call_args[0][0]
        pd.testing.assert_frame_equal(called_with, input_df)
