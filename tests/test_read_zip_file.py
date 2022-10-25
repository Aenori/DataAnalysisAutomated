from .helper import TEST_DATA_PATH
from src.read_zip_file import read_zip_file



def test_read_zip_file():
    df_co2, df_country_indicator, last_updated_at = read_zip_file(TEST_DATA_PATH)

    assert ('Country Code' in df_co2.columns)
    assert(df_co2.shape == (266, 67))
    assert(df_country_indicator.shape == (265, 5))
    assert(last_updated_at == "2022-09-16")

