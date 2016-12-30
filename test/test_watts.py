import os
import matplotlib as mpl
if 'DISPLAY' not in os.environ:
    mpl.use('Agg')
import watts


def _show(filename):
    unit, groups = watts.read_data(filename)
    # add average per second between the datetimes
    for group in groups:
        for meter in group['meters']:
            meter['aps'] = watts.average_per_second(
                meter['datetimes'],
                meter['values']
                )

    # merge across meters
    data = []
    for group in groups:
        datetimes_combined, averages_combined = \
            watts.merge_meters(group['meters'])
        data.append({
            'datetimes': datetimes_combined,
            'aps': averages_combined,
            'style': group['style'],
            })

    watts.show(unit, data)
    return


def test_electricity():
    _show('test_electricity.yml')


def test_water():
    _show('test_water.yml')
