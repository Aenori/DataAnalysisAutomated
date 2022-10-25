import os
import filecmp

import pandas as pd

from .helper import TEST_DATA_PATH
from src.read_zip_file import read_zip_file
from src.steps import clean_data, write_graphs, write_html_report


def test_clean_data():
    read_zip_file_output = read_zip_file(TEST_DATA_PATH)
    assert ('World' in read_zip_file_output[0]['Country Name'].values)
    df_co2_cleaned, last_updated_at_after = clean_data(read_zip_file_output)

    # Clean data should not change the last_updated_at
    assert (read_zip_file_output[2] == last_updated_at_after)

    # Clean data should remove all na and World (not a country)
    assert (not df_co2_cleaned.isnull().values.any())
    assert ('World' not in read_zip_file_output[0]['Country Name'].values)

    df_co2_cleaned.reset_index(inplace=True, drop=True)

    assert ((df_co2_cleaned == pd.read_csv('tests/data/co2_cleaned.csv')).all(axis=None))


def test_write_graph():
    df_co2_cleaned = pd.read_csv('tests/data/co2_cleaned.csv')
    assert(df_co2_cleaned.shape == (191, 20))

    for output in 'output/graph_1.png', 'output/graph_2.png':
        if os.path.isfile(output):
            os.remove(output)

    write_graphs((df_co2_cleaned, None))
    assert(filecmp.cmp('output/graph_1.png', 'tests/ref/graph_1.png'))
    assert(filecmp.cmp('output/graph_2.png', 'tests/ref/graph_2.png'))


def test_write_html_report():
    df_co2_cleaned = pd.read_csv('tests/data/co2_cleaned.csv')
    write_html_report((df_co2_cleaned, '2022-09-16'))

    assert (filecmp.cmp('output/report.html', 'tests/ref/report.html'))

