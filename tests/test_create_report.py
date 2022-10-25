from .helper import TEST_DATA_PATH
from .data_provider.data_provider_test import DataProviderTest
from src.create_report import create_report

def test_create_report():
    create_report(DataProviderTest(TEST_DATA_PATH))
