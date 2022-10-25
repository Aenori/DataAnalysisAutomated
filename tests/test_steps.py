import pandas as pd

from .helper import TEST_DATA_PATH
from src.read_zip_file import read_zip_file
from src.steps import clean_data

def test_clean_data():
    read_zip_file_output = read_zip_file(TEST_DATA_PATH)
    assert('World' in read_zip_file_output[0]['Country Name'].values)
    df_co2_cleaned, last_updated_at_after = clean_data(read_zip_file_output)

    # Clean data should not change the last_updated_at
    assert(read_zip_file_output[2] == last_updated_at_after)

    # Clean data should remove all na and World (not a country)
    assert(not df_co2_cleaned.isnull().values.any())
    assert ('World' not in read_zip_file_output[0]['Country Name'].values)

    df_co2_cleaned.reset_index(inplace=True, drop=True)

    assert((df_co2_cleaned == pd.read_csv('tests/data/co2_cleaned.csv')).all(axis=None))




