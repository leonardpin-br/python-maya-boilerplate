# -*- coding: utf-8 -*-
u"""Usefull functions for the user interface modules.

"""

__all__ = ['build_ui_qss_filenames']
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"

import os


def build_ui_qss_filenames(python_ui_file):
    u"""Builds the filenames of the ``.ui``, ``.qss`` files to be used in the
    class that is going to create the user interface.

    Args:
        python_ui_file (str): Full path, with extension, of the module where the
            class (that is going to create the user interface) is.

    Returns:
        tuple[str, str, str]: The ``.ui`` and ``.qss`` filenames (full paths),
        and the ``qss`` full directory path.
    """

    # The file must have the same name as the correspondent .ui and .qss files.
    PYTHON_UI_FILE = os.path.normpath(python_ui_file)
    DIR_NAME = os.path.dirname(PYTHON_UI_FILE)
    ROOT_DIR = os.path.dirname(os.path.dirname(DIR_NAME))

    # Filename and extension.
    PYTHON_FILE_BASENAME = os.path.basename(PYTHON_UI_FILE)

    # Directories building.
    RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")
    UI_DIR = os.path.join(RESOURCES_DIR, "ui")
    QSS_DIR = os.path.join(RESOURCES_DIR, "qss")

    # Unpacks the tupple.
    that_file_name, ext = PYTHON_FILE_BASENAME.split('.', 1)

    # Builds the filenames.
    UI_FILE = os.path.join(UI_DIR, (that_file_name + ".ui"))
    STYLESHEET_FILE = os.path.join(QSS_DIR, (that_file_name + ".qss"))

    return (UI_FILE, STYLESHEET_FILE, QSS_DIR)
