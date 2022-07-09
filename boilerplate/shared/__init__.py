# -*- coding: utf-8 -*-
u"""Package with useful functions that are shared by other packages.

Exports:
    ``functions``

    ``validation_functions``

Warning:
    The way of importing::

        from <package> import *

    is handy because it allows accessing the functions directly. For example::

        clear()

    Still, it is not recommended. It is advisable to write::

        # Yes, the package name.
        # The module name inside the package is not necessary.
        <package>.function_name()

    Here, inside ``__init__.py``, it is a good practice, though.

Note:
    The way of allowing this type of importing::

        from <package> import *

    is the construction below inside ``__init__.py``::

        __all__ = (functions.__all__ +
                    <module>.__all__)

    This is how it is done in this boilerplate's package::

        from . example_classes import *


        __all__ = (example_classes.__all__)

Note:
    Every file (module) should have a list of what is being "exported"::

        __all__ = [
            'ExampleSuperclass',
            'ExampleSubclass'
        ]

"""

from . functions import *
from . validation_functions import *
from . status_error_functions import *


__all__ = (functions.__all__ +
           validation_functions.__all__ +
           status_error_functions.__all__)
