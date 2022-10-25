import re

from jinja2 import Environment, FileSystemLoader

# regex to check the column names that are actually columns
YEAR_RE = re.compile('[0-9]{4}')

def _get_year_columns(df_co2):
    # NRO : here YEAR_RE.match(col) means checking the column name is made of 4 digits
    return [col for col in df_co2.columns if YEAR_RE.match(col)]

def clean_data(input_data):
    df_co2, df_countries, last_updated_at = input_data
    df_true_countries = df_countries[~df_countries['Region'].isna()]

    year_columns = _get_year_columns(df_co2)

    max_valid_values = df_co2[year_columns].count().max()
    valid_year_columns = [col for col in year_columns if df_co2[col].count() == max_valid_values]

    df_co2.drop(df_co2[~df_co2['Country Code'].isin(df_true_countries.index)].index, inplace=True)

    return df_co2[['Country Name', 'Country Code'] + valid_year_columns].dropna(), last_updated_at


def write_graphs(input_data):
    _write_graphs_1(input_data)
    _write_graphs_2(input_data)

    return input_data

def _write_graphs_1(input_data):
    df_co2 = input_data[0]
    fig = df_co2['2017'].hist().get_figure()
    fig.savefig('output/graph_1.png')
    fig.clear()


def _write_graphs_2(input_data):
    df_co2 = input_data[0]
    year_columns = _get_year_columns(df_co2)
    fig = df_co2[year_columns].mean().plot().get_figure()
    fig.savefig('output/graph_2.png')
    fig.clear()


def _get_dashboard_1(df_co2):
    year_columns = _get_year_columns(df_co2)
    largest_5_index = df_co2[year_columns[-1]].nlargest(5).index
    return df_co2.loc[largest_5_index, ['Country Name'] + year_columns[-5:]].to_html(index=False, classes="table table-striped")


def _get_dashboard_2(df_co2):
    year_columns = _get_year_columns(df_co2)

    for year_minus_1, year in zip(year_columns[-6:-1], year_columns[-5:]):
        df_co2[year + '_delta'] = df_co2[year] - df_co2[year_minus_1]

    delta_columns = [year + '_delta' for year in year_columns[-5:]]

    best_5_index = df_co2[delta_columns[-1]].nsmallest(5).index
    return df_co2.loc[best_5_index, ['Country Name'] + delta_columns].to_html(index=False, classes="table table-striped")



def write_html_report(input_data):
    df_co2, last_updated_at = input_data

    dashboard_1 = _get_dashboard_1(df_co2)
    dashboard_2 = _get_dashboard_2(df_co2)

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('report.j2')

    with open('output/report.html', 'w') as f:
        f.write(template.render(
            last_updated_at=last_updated_at,
            dashboard_1=dashboard_1,
            dashboard_2=dashboard_2
        ))

