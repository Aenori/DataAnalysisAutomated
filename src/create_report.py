import matplotlib.pyplot as plt

# NRO : the . of .read_zip_file means we are looking for a file in the
#  same folder
from .read_zip_file import read_zip_file
from .steps import clean_data, write_graphs, write_html_report

STEPS = [
    read_zip_file,
    clean_data,
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
