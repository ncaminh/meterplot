import argparse

import matplotlib.pyplot as plt

from .__about__ import __version__
from .helpers import average_per_second, merge_meters, read_data, show

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
    infile = args.infile

    unit, groups = read_data(infile)
    # add average per second between the datetimes
    for group in groups:
        for meter in group["meters"]:
            meter["aps"] = average_per_second(meter["datetimes"], meter["values"])

    # merge across meters
    data = []
    for group in groups:
        datetimes_combined, averages_combined = merge_meters(group["meters"])
        data.append(
            {
                "datetimes": datetimes_combined,
                "aps": averages_combined,
                "style": group["style"],
            }
        )

    show(unit, data)
    return
