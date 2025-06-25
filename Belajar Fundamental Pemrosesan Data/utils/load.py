import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def simpan_ke_csv(shop_df, filename):
    """Menyimpan DataFrame kedalam file CSV"""
    try:
        shop_df.to_csv(filename, index=False)
        print(f"Data disimpan sebagai {filename}")
    except Exception as e:
        raise ValueError(f"Gagal menyimpan sebagai CSV: {str(e)}")
def simpan_ke_sheets(shop_df: pd.DataFrame, credentials_file: str, spreadsheet_id: str, sheet_range='Sheet1!A1'):
    """Menyimpan DataFrame ke Google Sheets"""
    try:

            scope = ['https://www.googleapis.com/auth/spreadsheets']
            creds = Credentials.from_service_account_file(credentials_file, scopes=scope)
            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()

            # Ubah DataFrame menjadi list of lists (termasuk header)
            values = [shop_df.columns.tolist()] + shop_df.values.tolist()
            body = {
                'values': values
            }

            result = sheet.values().update(
                spreadsheetId=spreadsheet_id,
                range=sheet_range,
                valueInputOption='RAW',
                body=body
            ).execute()
            print(f"Data berhasil ditulis ke Google Sheets: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
            return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
    except Exception as e:
        raise ValueError(f"Gagal menulis data ke Google Sheets: {str(e)}")
def simpan_ke_db(shop_df, db_name, table_name, host, port, user, password):
    """Menyimpan DataFrame ke PostGreSQL database"""
    engine = None
    try:
        engine_url = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
        engine = create_engine(engine_url)

        shop_df.to_sql(table_name, engine, if_exists='replace', index=False, schema='public')
        print(f"Data di tambahkan ke table PostgreSQL database: {table_name}")
    except SQLAlchemyError as e:
        raise ValueError(f"Gagal menyimpan ke PostgreSQL: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error tak terduga saat menyimpan ke PostgreSQL: {str(e)}")
    finally:
        if engine is not None:
            engine.dispose()


