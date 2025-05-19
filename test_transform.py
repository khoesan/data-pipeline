import unittest
from utils.transform import clean_data

class TestTransform(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            {
                'Title': 'T-Shirt 1',
                'Price': '$10.00',
                'Rating': 'Rating: 4.5 / 5',
                'Colors': 'Colors: 3',
                'Size': 'Size: M',
                'Gender': 'Gender: Male',
                'Timestamp': '2025-05-12 10:00:00'
            },
            {
                'Title': 'Unknown Product',
                'Price': '$5.00',
                'Rating': 'Rating: 3.0 / 5',
                'Colors': 'Colors: 2',
                'Size': 'Size: S',
                'Gender': 'Gender: Female',
                'Timestamp': '2025-05-12 10:10:00'
            }
        ]

    def test_clean_data_removes_unknown_products(self):
        df = clean_data(self.raw_data)
        self.assertNotIn('Unknown Product', df['Title'].values)

    def test_price_conversion(self):
        df = clean_data(self.raw_data)
        self.assertEqual(df['Price'].iloc[0], 160000.0)

    def test_rating_conversion(self):
        df = clean_data(self.raw_data)
        self.assertIsInstance(df['Rating'].iloc[0], float)

    def test_colors_is_integer(self):
        df = clean_data(self.raw_data)
        self.assertEqual(df['Colors'].iloc[0], 3)

    def test_no_nulls(self):
        df = clean_data(self.raw_data)
        self.assertFalse(df.isnull().any().any())

if __name__ == '__main__':
    unittest.main()
