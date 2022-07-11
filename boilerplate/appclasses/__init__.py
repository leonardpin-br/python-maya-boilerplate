# -*- coding: utf-8 -*-
u"""Package with the classes used in this app.

This boilerplate has packages that are meant to be reused, like the
``activerecord`` and the ``shared`` packages.

This package (``appclasses``) has the classes specific to this app and would
change for every project that uses this boilerplate.

Exports:
    ``access_database``

"""

from . access_database import *


__all__ = (access_database.__all__)
