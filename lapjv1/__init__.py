"""Python wrapper of lapjv1
``python-lapjv1`` is a wrapper around a linear assignment problem solver by
Jonker and Volgenant.

Functions
---------

lap
    Find optimal (minimum-cost) assignment.
"""

import sys

__version__ = '0.1.dev0'

try:
    __lapjv1_SETUP__
except NameError:
    __lapjv1_SETUP__ = False
if __lapjv1_SETUP__:
    sys.stderr.write('Partial import of lapjv1 during the build process.\n')
else:
    from ._lapjv1 import lapjv1
    __all__ = ['lapjv1']
