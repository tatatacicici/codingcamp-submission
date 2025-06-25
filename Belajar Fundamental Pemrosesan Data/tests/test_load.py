
import pytest
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

from utils.load import simpan_ke_csv, simpan_ke_sheets, simpan_ke_db
from unittest.mock import patch, Mock, MagicMock, PropertyMock
import os
from sqlalchemy import create_engine

def test_simpan_ke_csv(tmp_path):
    df = pd.DataFrame({
        'Title': ['T-shirt 2'],
        'Price': [168000.0],
        'Rating': [3.9],
        'Colors': [3],
        'Size': ['M'],
        'Gender': ['Women'],
        'Timestamp': ['2025-05-06 12:00:00']
    })
    filename = tmp_path / "test.csv"
    simpan_ke_csv(df, filename)
    assert os.path.exists(filename)
    saved_df = pd.read_csv(filename)
    assert len(saved_df) == 1
    assert saved_df.iloc[0]['Title'] == 'T-shirt 2'
def test_simpan_ke_csv_failure(tmp_path):
    df = pd.DataFrame({
        'Title': ['T-shirt 2'],
        'Price': [168000.0]
    })
    with patch('pandas.DataFrame.to_csv', side_effect=Exception('Write Error')):
        with pytest.raises(ValueError, match="Gagal menyimpan sebagai CSV:.*"):
            simpan_ke_csv(df, tmp_path / "test.csv")


@patch('google.oauth2.service_account.Credentials.from_service_account_file')
@patch('googleapiclient.discovery.build', side_effect=Exception("API error"))
def test_simpan_ke_sheets_failure(mock_build, mock_creds_from_file):
    df = pd.DataFrame({
        'Title': ['T-shirt 2'],
        'Price': [168000.0]
    })

    mock_creds = Mock()
    mock_creds_from_file.return_value = mock_creds

    with pytest.raises(ValueError, match="Gagal menulis data ke Google Sheets:.*"):
        simpan_ke_sheets(df, 'google-sheets-api.json', 'TestSpreadsheetID')
@patch('utils.load.create_engine')
def test_simpan_ke_db(mock_create_engine):
    df = pd.DataFrame({
        'Title': ['T-shirt 2'],
        'Price': [168000.0],
        'Rating': [3.9],
        'Colors': [3],
        'Size': ['M'],
        'Gender': ['Women'],
        'Timestamp': ['2025-05-06 12:00:00']
    })

    mock_engine = Mock()
    mock_create_engine.return_value = mock_engine

    with patch.object(df, 'to_sql') as mock_to_sql:
        from utils.load import simpan_ke_db
        simpan_ke_db(df, 'test_db', 'products', 'localhost', '5432', 'user', 'pass')

        mock_create_engine.assert_called_once_with('postgresql://user:pass@localhost:5432/test_db')
        mock_to_sql.assert_called_once_with('products', mock_engine, if_exists='replace', index=False, schema='public')
        mock_engine.dispose.assert_called_once()


def test_simpan_ke_db_failure():
    df = pd.DataFrame({
        'Title': ['T-shirt 2'],
        'Price': [168000.0]
    })

    with patch('utils.load.create_engine', side_effect=SQLAlchemyError("DB error")):
        with pytest.raises(ValueError, match="Gagal menyimpan ke PostgreSQL:.*"):
            simpan_ke_db(df, 'test_db', 'products', 'localhost', '5432', 'user', 'pass')