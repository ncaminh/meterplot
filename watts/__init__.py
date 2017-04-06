# -*- coding: utf-8 -*-
#
'''Display energy consumption data.
'''

from watts.__about__ import (
    __author__,
    __email__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __status__
    )

from watts.helpers import *

import pipdated
if pipdated.needs_checking(__name__):
    print(pipdated.check(__name__, __version__))
