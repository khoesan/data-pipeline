import unittest
from unittest.mock import patch, Mock, mock_open
import pandas as pd

from utils.load import save_to_google_sheets  # pastikan path ini sesuai

class TestSaveToGoogleSheets(unittest.TestCase):
    @patch('utils.load.Credentials.from_service_account_file')
    @patch('utils.load.build')  # Pastikan sesuai seperti penjelasan di atas
    def test_save_to_google_sheets(self, mock_build, mock_from_service_account_file):
    # Buat dummy DataFrame
        df = pd.DataFrame({
            'Nama': ['Andi', 'Budi'],
            'Umur': [25, 30]
        })

        # Mock credentials
        mock_creds = Mock()
        mock_from_service_account_file.return_value = mock_creds

        # Mock Google Sheets API
        mock_service = Mock()
        mock_spreadsheets = Mock()
        mock_values = Mock()
        mock_clear = Mock()
        mock_update = Mock()

        mock_build.return_value = mock_service
        mock_service.spreadsheets.return_value = mock_spreadsheets
        mock_spreadsheets.values.return_value = mock_values
        mock_values.clear.return_value = mock_clear
        mock_clear.execute.return_value = {}
        mock_values.update.return_value = mock_update
        mock_update.execute.return_value = {}

        # Call function
        save_to_google_sheets(
            df,
            spreadsheet_id='dummy_spreadsheet_id',
            range_name='Sheet1!A1',
            credentials_file='fake_file.json'  # file ini tidak akan dibuka sungguhan karena dimock
        )

        # Assert semua fungsi mock dipanggil
        mock_from_service_account_file.assert_called_once()
        mock_values.clear.assert_called_once()
        mock_values.update.assert_called_once()
        print("✅ test_save_to_google_sheets passed.")

if __name__ == '__main__':
    unittest.main()