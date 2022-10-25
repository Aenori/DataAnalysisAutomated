import urllib.request
import os

WORLD_BANK_URL = "https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv"
TEMP_FILE_LOCATION = '/tmp/world_bank_co2.zip'

class WorldBankApiDataProvider:
    def __enter__(self):
        urllib.request.urlretrieve(WORLD_BANK_URL, TEMP_FILE_LOCATION)

        return TEMP_FILE_LOCATION

    def __exit__(self,  type_, value, tb):
        if os.path.exists(TEMP_FILE_LOCATION):
            os.remove(TEMP_FILE_LOCATION)
