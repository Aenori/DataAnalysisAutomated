import io

from zipfile import ZipFile
import pandas as pd

LAST_UPDATED_AT_LINE = 2


def read_zip_file(zip_file_path):
    zip_file = ZipFile(zip_file_path)

    for text_file in zip_file.infolist():
        if text_file.filename.startswith('API_EN.ATM.CO2E'):
            df_api = pd.read_csv(zip_file.open(text_file.filename), header=4)
            last_updated_at = extract_last_updated_at(text_file, zip_file)

        elif text_file.filename.startswith('Metadata_Country_'):
            df_country_meta_data = pd.read_csv(zip_file.open(text_file.filename))

    return df_api, df_country_meta_data, last_updated_at


def extract_last_updated_at(text_file, zip_file):
    with io.TextIOWrapper(zip_file.open(text_file.filename), encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == LAST_UPDATED_AT_LINE:
                # [1:-1] to remove first and last " character
                return line.split(",")[1][1:-1]
