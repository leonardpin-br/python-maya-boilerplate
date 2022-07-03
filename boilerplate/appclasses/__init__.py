# -*- coding: utf-8 -*-
u"""Package with my custom modules.

Exports:
    ``access_database``

Note:
    The way of importing::

        from <package> import *

    is handy because it allows accessing the functions directly. For example::

        clear()

    Still, it is not recommended. It is advisable to write::

        <package>.function_name()

    Here, inside ``__init__.py``, it is a good practice, though.

Note:
    The way of allowing this type of importing::

        from <package> import *

    is the construction below inside ``__init__.py``::

        __all__ = (utils.__all__ +
                    <package>.__all__)

    This is how it is done in this boilerplate's package::

        from . example_classes import *


        __all__ = (example_classes.__all__)

Note:
    Every file should have a list of what is being "exported"::

        __all__ = [
            'ExampleSuperclass',
            'ExampleSubclass'
        ]

"""

from . access_database import *


__all__ = (access_database.__all__)
