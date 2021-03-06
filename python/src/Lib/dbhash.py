"""Provide a (g)dbm-compatible interface to bsddb.hashopen."""

import sys
if sys.py3kwarning:
    import warnings
    warnings.warnpy3k("in 3.x, dbhash has been removed", DeprecationWarning, 2)
try:
    import bsddb
except ImportError:
    # prevent a second import of this module from spuriously succeeding
    del sys.modules[__name__]
    raise

__all__ = ["error","open"]

error = bsddb.error                     # Exported for anydbm

def open(file, flag = 'r', mode=0666):
    return bsddb.hashopen(file, flag, mode)
