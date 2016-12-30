

def test_import():
    import os
    import matplotlib as mpl
    if 'DISPLAY' not in os.environ:
        mpl.use('Agg')
    import watts
    return
