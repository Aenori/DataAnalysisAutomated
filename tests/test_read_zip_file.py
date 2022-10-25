from src.read_zip_file import read_zip_file
from .helper import TEST_DATA_PATH


def test_version():
    df_co2, df_country_indicator = read_zip_file(TEST_DATA_PATH)
    assert(df_co2.shape == (264, 67))
    assert(df_country_indicator.shape ==(265, 6))
