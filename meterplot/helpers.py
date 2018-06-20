# -*- coding: utf-8 -*-
#
from itertools import groupby

import matplotlib.pyplot as plt
import yaml


def read_data(filename):
    stream = open(filename, "r")
    docs = yaml.load_all(stream)
    d = [doc for doc in docs]
    assert len(d) == 1
    doc = d[0]

    groups = []
    for group in doc["groups"]:
        groups.append({"style": group["style"], "meters": []})
        for meter in group["meters"]:
            # assert that the dates are sorted chronologically
            datetimes = [datum["date"] for datum in meter["data"]]
            for k in range(len(datetimes) - 1):
                diff = datetimes[k + 1] - datetimes[k]
                diff_in_secs = diff.days * 24 * 3600 + diff.seconds
                assert diff_in_secs > 0

            groups[-1]["meters"].append(
                {
                    "datetimes": datetimes,
                    "values": [datum["value"] for datum in meter["data"]],
                }
            )

    return doc["unit"], groups


def average_per_second(datetimes, values):
    """Input: datetime, values
    Output: average value per second between the datetimes
    """
    assert len(datetimes) == len(values)

    aps = []
    for k in range(len(datetimes) - 1):
        diff = datetimes[k + 1] - datetimes[k]
        diff_in_secs = diff.days * 24 * 3600 + diff.seconds
        assert diff_in_secs > 0

        aps.append((values[k + 1] - values[k]) / float(diff_in_secs))

    return aps


def merge_meters(meters):
    # merge datetimes
    datetimes_combined = sorted(sum([meter["datetimes"] for meter in meters], []))

    # now iterate over the intervals and collect the average values
    averages_combined = [0.0] * (len(datetimes_combined) - 1)
    for meter in meters:
        for k in range(len(meter["datetimes"]) - 1):
            # find the beginning of the interval
            k0 = datetimes_combined.index(meter["datetimes"][k])
            k1 = datetimes_combined.index(meter["datetimes"][k + 1])
            # add the average value to all intervals between beginning and end
            for kk in range(k0, k1):
                averages_combined[kk] += meter["aps"][k]

    return datetimes_combined, averages_combined


def harmonize_groups(groups):
    X_combined = sorted(sum([group["datetimes"] for group in groups], []))
    X_combined = [x[0] for x in groupby(X_combined)]

    for group in groups:
        group["combined data"] = [0.0] * (len(X_combined) - 1)
        for i in range(len(X_combined) - 1):
            z = zip(group["datetimes"], group["aps"])
            for t, val in reversed(list(z)):
                if t <= X_combined[i]:
                    group["combined data"][i] = val
                    break
    return X_combined, groups


# pylint: disable=too-many-locals
def show(unit, groups):
    # harmonize x values across all groups
    X_combined, groups = harmonize_groups(groups)

    # duplicate all interior values for plotting the discontinuous data set
    x = (
        [X_combined[0]]
        + [d for d in X_combined[1:-1] for _ in (0, 1)]
        + [X_combined[-1]]
    )

    # set up axes
    ax1 = plt.gca()
    ax1.set_xlim(min(x), max(x))
    ax2 = ax1.twinx()
    ax2.set_xlim(min(x), max(x))

    # We need to tie the actual data to the second axes. This is because
    # everything from the second axos has a higher z-value as everything from
    # the first axis, including the data. Even if we decide to draw grid lines
    # behind the plot, grid lines of the second axis will always overlap the
    # plot if it's connected ot the first axis. See
    # <https://github.com/matplotlib/matplotlib/issues/7984>.
    # Hence, scale the data to the units of the second axis.
    if unit == "kWh":
        # kWh per second -> watts
        ax2.set_ylabel("W")
        factor = 1000 * 3600
    else:
        assert unit == "m^3"
        # m^3 per second -> liters per day
        ax2.set_ylabel("liters per day")
        factor = 1000 * 3600 * 24
    y = [
        [val * factor for val in group["combined data"] for _ in (0, 1)]
        for group in groups
    ]

    ysum = [0.0] * len(y[0])
    # pylint: disable=consider-using-enumerate
    for k in range(len(y)):
        for i in range(len(y[k])):
            ysum[i] += y[k][i]
    ytop = 1.1 * max(ysum)
    ax2.set_ylim(0.0, ytop)

    colors = []
    for group in groups:
        colors.append(group["style"]["color"])

    ax2.stackplot(x, y, colors=colors)

    # Set the scale of the first axis. Since the data is connected to the
    # second axis, we could scale however we want here without distorting the
    # plot.
    if unit == "kWh":
        # Watts -> kWh per year
        ax1.set_ylabel("kWh per year")
        ax1.set_ylim(0.0, ytop * 24 * 365 / 1000.0)
    else:
        assert unit == "m^3"
        # liters per day -> m^3 per year
        ax1.set_ylabel("m^3 per year")
        ax1.set_ylim(0.0, ytop * 365.0 / 1000.0)

    return
