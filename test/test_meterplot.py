# -*- coding: utf-8 -*-
#
import meterplot


def _show(filename):
    unit, groups = meterplot.read_data(filename)
    # add average per second between the datetimes
    for group in groups:
        for meter in group['meters']:
            meter['aps'] = meterplot.average_per_second(
                meter['datetimes'],
                meter['values']
                )

    # merge across meters
    data = []
    for group in groups:
        datetimes_combined, averages_combined = \
            meterplot.merge_meters(group['meters'])
        data.append({
            'datetimes': datetimes_combined,
            'aps': averages_combined,
            'style': group['style'],
            })

    meterplot.show(unit, data)
    return


def test_electricity():
    _show('test_electricity.yml')


def test_water():
    _show('test_water.yml')
