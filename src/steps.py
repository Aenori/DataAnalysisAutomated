import matplotlib.pyplot as plt
import re

# regex to check the column names that are actually columns
YEAR_RE = re.compile('[0-9]{4}')


def clean_data(input):
    df_co2, df_countries, last_updated_at = input
    df_true_countries = df_countries[~df_countries['Region'].isna()]

    year_columns = [col for col in df_co2.columns if YEAR_RE.match(col)]

    max_valid_values = df_co2[year_columns].count().max()
    valid_year_columns = [col for col in year_columns if df_co2[col].count() == max_valid_values]

    df_co2.drop(df_co2[~df_co2['Country Code'].isin(df_true_countries.index)].index, inplace=True)

    return df_co2[['Country Name', 'Country Code'] + valid_year_columns].dropna(), last_updated_at


def construct_dashboards(input_data):
    pass


def write_graphs(input_data):
    pass


def _write_graphs_1(input_data):
    df_co2, _ = input_data
    df_co2['2017'].hist().get_figure().savefig('output/graph_1.png')


def _write_graphs_2(input_data):
    df_co2, _ = input_data
    year_columns = [col for col in df_co2.columns if YEAR_RE.match(col)]
    df_co2[year_columns].mean().plot().get_figure().savefig('output/graph_2.png')

def write_html_report(input_data):
    pass
