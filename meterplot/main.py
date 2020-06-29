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
    values = numpy.array([item["value"] for item in doc["data"]]).T

    if len(values.shape) > 1:
        values = values.T

    return doc["unit"], datetimes, values


def average_per_second(datetimes, values):
    """Input: datetime, values
    Output: average value per second between the datetimes
    """
    assert len(datetimes) == len(values)

    diff = datetimes[1:] - datetimes[:-1]
    diff_in_secs = numpy.array([d.days * 24 * 3600 + d.seconds for d in diff])
    assert numpy.all(diff_in_secs > 0)
    return ((values[1:] - values[:-1]).T / diff_in_secs).T


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
    vals = numpy.repeat(values, 2)

    ax2.stackplot(dt, vals)

    # Set the scale of the first axis. Since the data is connected to the second axis,
    # we could scale however we want here without distorting the plot.
    if unit == "kWh":
        # Watts -> kWh per year
        ax1.set_ylabel("kWh per year")
        ylim = ax2.get_ylim()
        ax1.set_ylim(ylim[0] * 24 * 365 / 1000.0, ylim[1] * 24 * 365 / 1000.0)
    else:
        assert unit == "m^3"
        # liters per day -> m^3 per year
        ax1.set_ylabel("m^3 per year")
        # ax1.set_ylim(0.0, ytop * 365.0 / 1000.0)
