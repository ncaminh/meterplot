#!/usr/bin/env python
import matplotlib.pyplot as plt
from itertools import groupby
import yaml


def read_data(filename):
    stream = open(filename, 'r')
    docs = yaml.load_all(stream)
    d = [doc for doc in docs]
    assert len(d) == 1
    doc = d[0]

    groups = []
    for group in doc['groups']:
        groups.append({
            'style': group['style'],
            'meters': [],
            })
        for meter in group['meters']:
            # assert that the dates are sorted chronologically
            datetimes = [datum['date'] for datum in meter['data']]
            for k in range(len(datetimes) - 1):
                diff = datetimes[k+1] - datetimes[k]
                diff_in_secs = diff.days * 24 * 3600 + diff.seconds
                assert diff_in_secs > 0

            groups[-1]['meters'].append({
                'datetimes': datetimes,
                'values': [datum['value'] for datum in meter['data']],
                })

    return doc['unit'], groups


def average_per_second(datetimes, values):
    '''Input: datetime, values
    Output: average value per second between the datetimes
    '''
    assert len(datetimes) == len(values)

    aps = []
    for k in range(len(datetimes) - 1):
        diff = datetimes[k+1] - datetimes[k]
        diff_in_secs = diff.days * 24 * 3600 + diff.seconds
        assert diff_in_secs > 0

        aps.append(
            (values[k+1] - values[k]) / float(diff_in_secs)
            )

    return aps


def merge_meters(meters):
    # merge datetimes
    datetimes_combined = sorted(sum(
        [meter['datetimes'] for meter in meters], []
        ))

    # now iterate over the intervals and collect the average values
    averages_combined = [0.0] * (len(datetimes_combined) - 1)
    for meter in meters:
        for k in range(len(meter['datetimes']) - 1):
            # find the beginning of the interval
            k0 = datetimes_combined.index(meter['datetimes'][k])
            k1 = datetimes_combined.index(meter['datetimes'][k+1])
            # add the average value to all intervals between beginning and end
            for kk in range(k0, k1):
                averages_combined[kk] += meter['aps'][k]

    return datetimes_combined, averages_combined


def harmonize_groups(groups):
    X_combined = sorted(sum(
        [group['datetimes'] for group in groups],
        []
        ))
    X_combined = [x[0] for x in groupby(X_combined)]

    for group in groups:
        group['combined data'] = [0.0] * (len(X_combined) - 1)
        for i in range(len(X_combined) - 1):
            z = zip(group['datetimes'], group['aps'])
            for t, val in reversed(list(z)):
                if t <= X_combined[i]:
                    group['combined data'][i] = val
                    break
    return X_combined, groups


def show(unit, groups):
    # harmonize x values across all groups
    X_combined, groups = harmonize_groups(groups)

    # duplicate all interior values for plotting the discontinuous data set
    dt = X_combined
    x = [dt[0]] + \
        [d for d in dt[1:-1] for _ in (0, 1)] + \
        [dt[-1]]

    y = [
        [
            # average per second -> average per year
            val * (365 * 24 * 3600)
            for val in group['combined data']
            for _ in (0, 1)
        ]
        for group in groups
        ]

    colors = []
    for group in groups:
        colors.append(group['style']['color'])

    plt.stackplot(
        x, y,
        colors=colors
        )

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.set_xlim(min(x), max(x))

    ysum = [0.0] * len(y[0])
    for k in range(len(y)):
        for i in range(len(y[k])):
            ysum[i] += y[k][i]

    ytop = 1.1 * max(ysum)
    ax1.set_ylim(0, ytop)

    ax1.set_ylabel('%s per year' % unit)

    assert unit in ['kWh', 'm^3']
    if unit == 'kWh':
        ax2.set_ylim(0, ytop * 1000 / (24 * 365.))
        ax2.set_ylabel('W')
    else:  # unit == 'm^3'
        ax2.set_ylim(0, ytop * 1000 / 365.)
        ax2.set_ylabel('liters per day')

    return
