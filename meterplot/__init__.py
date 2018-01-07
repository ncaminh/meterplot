# -*- coding: utf-8 -*-
#
'''Display energy consumption data.
'''

from .__about__ import (
    __author__,
    __email__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __status__
    )

from .helpers import *

try:
    import pipdate
except ImportError:
    pass
else:
    if pipdate.needs_checking(__name__):
        print(pipdate.check(__name__, __version__))
