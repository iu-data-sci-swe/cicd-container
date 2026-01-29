import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the module
import importlib.util
spec = importlib.util.spec_from_file_location("fraud_prediction", os.path.join(os.path.dirname(__file__), '..', 'src', 'fraud_prediction.py'))
fraud_prediction_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fraud_prediction_module)
run_model = fraud_prediction_module.run_model
create_input_dataframe = fraud_prediction_module.create_input_dataframe


class TestCreateInputDataFrame:
    """Test suite for the create_input_dataframe function."""
    
    @pytest.fixture(autouse=True)
    def setup_encoders(self):
        """Setup mock encoders before each test."""
        # Mock the encoder transforms
        self.enc_product_patcher = patch.object(fraud_prediction_module, 'enc_product')
        self.enc_hour_patcher = patch.object(fraud_prediction_module, 'enc_hour')
        self.enc_gender_patcher = patch.object(fraud_prediction_module, 'enc_gender')
        self.enc_state_patcher = patch.object(fraud_prediction_module, 'enc_state')
        
        self.mock_enc_product = self.enc_product_patcher.start()
        self.mock_enc_hour = self.enc_hour_patcher.start()
        self.mock_enc_gender = self.enc_gender_patcher.start()
        self.mock_enc_state = self.enc_state_patcher.start()
        
        # Setup column name mocks
        self.product_cols_patcher = patch.object(fraud_prediction_module, 'product_cols', ['product_Electronics', 'product_Clothing'])
        self.hour_cols_patcher = patch.object(fraud_prediction_module, 'hour_cols', ['hour_7', 'hour_8'])
        self.gender_cols_patcher = patch.object(fraud_prediction_module, 'gender_cols', ['gender_M', 'gender_F'])
        self.state_cols_patcher = patch.object(fraud_prediction_module, 'state_cols', ['state_CA', 'state_NY'])
        
        self.product_cols_patcher.start()
        self.hour_cols_patcher.start()
        self.gender_cols_patcher.start()
        self.state_cols_patcher.start()
        
        yield
        
        # Cleanup
        self.enc_product_patcher.stop()
        self.enc_hour_patcher.stop()
        self.enc_gender_patcher.stop()
        self.enc_state_patcher.stop()
        self.product_cols_patcher.stop()
        self.hour_cols_patcher.stop()
        self.gender_cols_patcher.stop()
        self.state_cols_patcher.stop()
    
    def setup_successful_encoders(self):
        """Configure mocks for successful encoding."""
        self.mock_enc_product.transform.return_value = np.array([[1, 0]])
        self.mock_enc_hour.transform.return_value = np.array([[1, 0]])
        self.mock_enc_gender.transform.return_value = np.array([[1, 0]])
        self.mock_enc_state.transform.return_value = np.array([[1, 0]])
    
    def test_create_input_dataframe_success(self):
        """Test successful creation of input dataframe with valid inputs."""
        self.setup_successful_encoders()
        
        result = create_input_dataframe(
            amount=100.0,
            product_category='Electronics',
            time_str='2024-01-15T14:30:00',
            address_state='CA',
            gender='M',
            credit_score=750
        )
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 1
        assert 'amount' in result.columns
    
    def test_create_input_dataframe_returns_dataframe(self):
        """Test that the function returns a DataFrame."""
        self.setup_successful_encoders()
        
        result = create_input_dataframe(
            amount=50.0,
            product_category='Clothing',
            time_str='2024-01-15T09:00:00',
            address_state='NY',
            gender='F',
            credit_score=800
        )
        
        assert isinstance(result, pd.DataFrame)
    
    def test_create_input_dataframe_includes_amount(self):
        """Test that the returned dataframe includes the amount column."""
        self.setup_successful_encoders()
        
        amount = 150.0
        result = create_input_dataframe(
            amount=amount,
            product_category='Electronics',
            time_str='2024-01-15T10:00:00',
            address_state='CA',
            gender='M',
            credit_score=700
        )
        
        assert 'amount' in result.columns
        assert result['amount'].iloc[0] == amount
    
    def test_create_input_dataframe_invalid_product_category(self):
        """Test error handling for unknown product category."""
        self.mock_enc_product.transform.side_effect = ValueError("Unknown category")
        self.setup_successful_encoders()
        
        with pytest.raises(ValueError, match="Unknown product category"):
            create_input_dataframe(
                amount=100.0,
                product_category='InvalidProduct',
                time_str='2024-01-15T14:30:00',
                address_state='CA',
                gender='M',
                credit_score=750
            )
    
    def test_create_input_dataframe_invalid_gender(self):
        """Test error handling for unknown gender."""
        self.mock_enc_product.transform.return_value = np.array([[1, 0]])
        self.mock_enc_gender.transform.side_effect = ValueError("Unknown gender")
        self.mock_enc_hour.transform.return_value = np.array([[1, 0]])
        self.mock_enc_state.transform.return_value = np.array([[1, 0]])
        
        with pytest.raises(ValueError, match="Unknown gender"):
            create_input_dataframe(
                amount=100.0,
                product_category='Electronics',
                time_str='2024-01-15T14:30:00',
                address_state='CA',
                gender='X',
                credit_score=750
            )
    
    def test_create_input_dataframe_invalid_state(self):
        """Test error handling for unknown state."""
        self.mock_enc_product.transform.return_value = np.array([[1, 0]])
        self.mock_enc_gender.transform.return_value = np.array([[1, 0]])
        self.mock_enc_hour.transform.return_value = np.array([[1, 0]])
        self.mock_enc_state.transform.side_effect = ValueError("Unknown state")
        
        with pytest.raises(ValueError, match="Unknown state"):
            create_input_dataframe(
                amount=100.0,
                product_category='Electronics',
                time_str='2024-01-15T14:30:00',
                address_state='InvalidState',
                gender='M',
                credit_score=750
            )
    
    def test_create_input_dataframe_invalid_time_format(self):
        """Test error handling for invalid time format."""
        self.setup_successful_encoders()
        
        with pytest.raises(ValueError, match="Invalid time format"):
            create_input_dataframe(
                amount=100.0,
                product_category='Electronics',
                time_str='not-a-valid-time',
                address_state='CA',
                gender='M',
                credit_score=750
            )
    
    def test_create_input_dataframe_extracts_hour_correctly(self):
        """Test that the correct hour is extracted from timestamp."""
        self.setup_successful_encoders()
        
        create_input_dataframe(
            amount=100.0,
            product_category='Electronics',
            time_str='2024-01-15T14:30:00',
            address_state='CA',
            gender='M',
            credit_score=750
        )
        
        # Verify hour_encoder was called with hour 14
        self.mock_enc_hour.transform.assert_called()
        call_args = self.mock_enc_hour.transform.call_args
        assert call_args[0][0][0][0] == 14
    
    def test_create_input_dataframe_single_row(self):
        """Test that the returned dataframe has exactly one row."""
        self.setup_successful_encoders()
        
        result = create_input_dataframe(
            amount=100.0,
            product_category='Electronics',
            time_str='2024-01-15T14:30:00',
            address_state='CA',
            gender='M',
            credit_score=750
        )
        
        assert len(result) == 1
    
