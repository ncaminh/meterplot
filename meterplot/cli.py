import argparse

import matplotlib.pyplot as plt

from .__about__ import __version__
from .main import average_per_second, read_data, show

plt.style.use("ggplot")


def _get_parser():
    parser = argparse.ArgumentParser(description="Show energy consumption data")
    parser.add_argument("infile", type=str, help="input data YAML file")
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="%(prog)s " + (f"(version {__version__})"),
    )
    return parser


def main(argv=None):
    parser = _get_parser()
    args = parser.parse_args(argv)
    unit, datetimes, values = read_data(args.infile)
    averages = average_per_second(datetimes, values)
    show(unit, datetimes, averages)
