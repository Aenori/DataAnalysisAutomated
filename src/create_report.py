import matplotlib.pyplot as plt

from .read_zip_file import read_zip_file
from .steps import clean_data, construct_dashboards, write_graphs, write_html_report

STEPS = [
    read_zip_file,
    clean_data,
    construct_dashboards,
    write_graphs,
    write_html_report
]


def create_report(data_provider):
    with data_provider as filename:
        create_report_from_data(filename)


def create_report_from_data(filename):
    input = filename
    configure_matplotlib()

    for step in STEPS:
        input = step(input)


def configure_matplotlib():
    plt.rcParams['figure.figsize'] = [13, 6]
