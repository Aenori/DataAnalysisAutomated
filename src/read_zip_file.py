from zipfile import ZipFile
import pandas as pd


def read_zip_file(zip_file_path):
    zip_file = ZipFile(zip_file_path)

    for text_file in zip_file.infolist():
        if text_file.filename.startswith('API_EN.ATM.CO2E'):
            df_api = pd.read_csv(zip_file.open(text_file.filename), header=4)
        elif text_file.filename.startswith('Metadata_Country_'):
            df_country_meta_data = pd.read_csv(zip_file.open(text_file.filename))

    return df_api, df_country_meta_data
