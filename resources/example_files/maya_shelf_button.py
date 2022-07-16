# -*- coding: utf-8 -*-
u"""Maya shelf button for this app to run.

This is a (Maya) shelf button example to make this code run without conflict
with the Sphinx's sphinx-apidoc tool.
"""

import sys

module_path = 'E:\\cloud\\Backup\\Libraries\\scripts\\maya\\python-maya-boilerplate\\src'

# Se o caminho não faz parte do path:
for path in sys.path:
    if path == module_path:
        break
else:
    sys.path.insert(0, module_path)

import main
reload(main)