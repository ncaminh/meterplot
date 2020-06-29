from pathlib import Path

import meterplot


def _show(filename):
    this_dir = Path(__file__).resolve().parent
    unit, datetimes, values = meterplot.read_data(this_dir / filename)
    averages = meterplot.average_per_second(datetimes, values)
    meterplot.show(unit, datetimes, averages)


def test_electricity():
    _show("test_electricity.yml")


def test_water():
    _show("test_water.yml")
