import matplotlib.pyplot as plt
import numpy
import yaml


def read_data(filename):
    stream = open(filename, "r")
    docs = yaml.load_all(stream, Loader=yaml.SafeLoader)
    d = [doc for doc in docs]
    assert len(d) == 1
    doc = d[0]

    datetimes = numpy.array([item["date"] for item in doc["data"]])
    values = numpy.array([item["value"] for item in doc["data"]])

    return doc["unit"], datetimes, values


def average_per_second(datetimes, values):
    assert len(datetimes) == len(values)

    diff = datetimes[1:] - datetimes[:-1]
    diff_in_secs = numpy.array([d.days * 24 * 3600 + d.seconds for d in diff])
    assert numpy.all(diff_in_secs > 0)

    # if the value is negative, it means that a meter change has occurred
    diff_vals = values[1:] - values[:-1]
    is_neg = diff_vals < 0
    diff_vals[is_neg] = values[1:][is_neg]

    return (diff_vals.T / diff_in_secs).T


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()


def plot(unit, datetimes, values):
    # set up axes
    ax1 = plt.gca()
    ax1.set_xlim(min(datetimes), max(datetimes))
    ax2 = ax1.twinx()
    ax2.set_xlim(min(datetimes), max(datetimes))

    # We need to tie the actual data to the second axes. This is because everything from
    # the second axis has a higher z-value than everything from the first axis,
    # including the data. Even if we decide to draw grid lines behind the plot, grid
    # lines of the second axis will always overlap the plot if it's connected to the
    # first axis. See <https://github.com/matplotlib/matplotlib/issues/7984>. Hence,
    # scale the data to the units of the second axis.
    if unit == "kWh":
        # kWh per second -> watts
        ax2.set_ylabel("W")
        factor = 1000 * 3600
    else:
        assert unit == "m^3"
        # m^3 per second -> liters per day
        ax2.set_ylabel("liters per day")
        factor = 1000 * 3600 * 24

    values *= factor

    # prepare data for plotting
    dt = numpy.repeat(datetimes, 2)[1:-1]
    vals = numpy.repeat(values, 2, axis=0)

    ax2.stackplot(dt, vals.T)

    # Set the scale of the first axis. Since the data is connected to the second axis,
    # we could scale however we want here without distorting the plot.
    ylim = numpy.array(ax2.get_ylim())
    if unit == "kWh":
        # Watts -> kWh per year
        ax1.set_ylabel("kWh per year")
        ax1.set_ylim(*(ylim * 24 * 365 / 1000))
    else:
        assert unit == "m^3"
        # liters per day -> m^3 per year
        ax1.set_ylabel("m^3 per year")
        ax1.set_ylim(*(ylim * 365 / 1000))
