# -*- coding: utf-8 -*-
#
"""Display energy consumption data.
"""
from __future__ import print_function

from . import cli
from .__about__ import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __status__,
    __version__,
)
from .helpers import average_per_second, merge_meters, read_data, show

__all__ = [
    "__author__",
    "__email__",
    "__copyright__",
    "__license__",
    "__version__",
    "__status__",
    "cli",
    "read_data",
    "average_per_second",
    "merge_meters",
    "show",
]

try:
    import pipdate
except ImportError:
    pass
else:
    if pipdate.needs_checking(__name__):
        print(pipdate.check(__name__, __version__), end="")
