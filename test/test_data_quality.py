import pandas as pd


class TestModelQuality:
    """Test for data quality"""

    def test_data_quality(self):
        """Test that the model data quality is as expected."""
    
        # Load the dataset
        df = pd.read_csv('data/fraud.csv.bz2')

        assert df.shape[0] > 10000, "Dataset should have more than 10,000 rows"
        assert df.shape[1] == 7, "Dataset should have exactly 7 columns"
        assert df['amount'].min() >= 0, "Transaction amounts should be non-negative"
        assert df['fraud'].isin([False, True]).all(), "Fraud column should only contain True or False"
