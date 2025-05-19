import unittest
import pandas as pd
from utils.extract import extract_data

def test_extract_data_returns_dataframe():
    df = extract_data()
    assert not df.empty
    assert isinstance(df, pd.DataFrame)

class TestExtract(unittest.TestCase):
    def test_extract_returns_list(self):
        data = extract_data()
        self.assertIsInstance(data, pd.DataFrame)
        self.assertIsInstance(data.iloc[0].to_dict(), dict)

if __name__ == '__main__':
    unittest.main()
