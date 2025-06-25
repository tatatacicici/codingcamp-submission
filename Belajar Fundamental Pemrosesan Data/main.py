import pandas as pd
from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import simpan_ke_csv, simpan_ke_sheets, simpan_ke_db

def main():
    try:
        #ekstrak
        print("Mulai Ekstraksi")
        data = scrape_main()

        #transformasi
        print("Mulai Transformasi data")
        transformed_data = transform_data(data)

        #Load
        print("Mulai Load data")
        simpan_ke_csv(transformed_data, 'products.csv')
        simpan_ke_sheets(transformed_data, 'google-sheets-api.json','1qllytiyXDzS1qbmQ-JtITj9GBoZsv1QqDQevmv1NCME')
        simpan_ke_db(transformed_data, 'fashion_db','products','localhost','5432','postgres','admin123')

        print("Proses ETL pipeline berhasil!")
    except Exception as e:
        print(f"Proses ETL gagal: {str(e)}")
if __name__ == "__main__":
    main()