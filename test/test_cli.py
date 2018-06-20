# -*- coding: utf-8 -*-
#
import os

import meterplot


def test_cli():
    this_dir = os.path.dirname(os.path.realpath(__file__))

    meterplot.cli.main([os.path.join(this_dir, "test_electricity.yml")])
    return
