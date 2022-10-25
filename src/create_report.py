from .read_zip_file import read_zip_file


def create_report(data_provider):
    with data_provider as filename:
        _create_report_from_data(filename)


def _create_report_from_data(filename):
    df_co2, df_countries, last_updated_at = read_zip_file(filename)
