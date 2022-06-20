# -*- coding: utf-8 -*-
r"""Class to be instantiated from all the others that access the database.

A shelf button button should be created and this code executed from there.

Note:
	Defining the window icon does not work in Maya.
    Qt Designer shows it perfectly on the preview, but Maya does not.

Note:
    It is not necessary to use background-image in the ``.qss`` when inserting
    images into the window (like a logo). When using QPixmap (QLabel > pixmap
    in Qt Designer), the ``.qrc`` should be compiled into ``.py``. Then, that
    new module **must be imported** in the module that creates the ui.

Examples:
    How to convert from ``.ui`` to ``.py`` using PySide2 integrated in Maya (**must be run in Powershell**)::

    &"C:\Program Files\Autodesk\Maya2020\bin\mayapy.exe" "C:\Program Files\Autodesk\Maya2020\bin\pyside2-uic" -o .\test.py .\test.ui

    How to convert from ``.qrc`` to ``py`` using PySide2 integrated in Maya (**must be run in Powershell and must swap the double backslashes for single slashes**)::

    &"C:\Program Files\Autodesk\Maya2020\bin\pyside2-rcc.exe" .\resources\\ui_resources.qrc -o .\boilerplate\\userinterface\\ui_resources.py

References:
    `Example Google Style Python Docstrings`_

    `Using Qt Designer in maya`_

    `Maya | Qt DesignerでサクッとUI作っちゃおう！`_

    `closing qDialog (if exists) in pySide`_

    `Pyside2 UI Example for Maya`_

    `Applying styles to PyQt widgets from external stylesheet`_

    `PyQt and PySide Widget Best Practices`_

    `Working with PySide in Maya`_

    `How can I open multiple files using "with open" in Python?`_

    `[Maya Python] Display .ui created by Qt Designer in Maya`_

    `Calling a MEL script with Python`_

    `Pymel and QT using Designer Noob Question`_

    `Using QT Designer for MEL Interfaces`_

    `Maya QT interfaces in a class`_

    `Using PySide2 to develop Maya Plug-in Series I\: QT Designer to design GUI, pyside-uic to convert. ui file to. py file`_

    `TypeError\: 'encoding' is an invalid keyword argument for this function`_

    `Building Sphinx documentation for unfriendly code`_

    `Error when autodocumenting pymel code with Sphinx`_

    `Pyside2 with Qt Designer - Resource(icons) ignored when using QUiLoader()`_

    `Thread\: QUiLoader & *.qrc files?`_

.. _Example Google Style Python Docstrings:
   https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
.. _Using Qt Designer in maya:
   https://forums.autodesk.com/t5/maya-programming/using-qt-designer-in-maya/m-p/10116170/highlight/true#M13148
.. _Maya | Qt DesignerでサクッとUI作っちゃおう！:
   https://www.youtube.com/watch?v=rhtLC5kKoBI&t=618s
.. _closing qDialog (if exists) in pySide:
   https://stackoverflow.com/questions/42281843/closing-qdialog-if-exists-in-pyside#answer-42600180
.. _Pyside2 UI Example for Maya:
   https://luckcri.blogspot.com/2018/04/pyside2-ui-example-for-maya.html
.. _Applying styles to PyQt widgets from external stylesheet:
   https://stackoverflow.com/questions/47621172/applying-styles-to-pyqt-widgets-from-external-stylesheet
.. _PyQt and PySide Widget Best Practices:
   https://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=__files_GUID_66ADA1FF_3E0F_469C_84C7_74CEB36D42EC_htm
.. _Working with PySide in Maya:
   https://help.autodesk.com/view/MAYAUL/2017/ENU/?guid=__files_GUID_3F96AF53_A47E_4351_A86A_396E7BFD6665_htm
.. _How can I open multiple files using "with open" in Python?:
   https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python
.. _[Maya Python] Display .ui created by Qt Designer in Maya:
   https://linuxtut.com/en/7d2ab808b5cf3f2d9707/
.. _Calling a MEL script with Python:
   https://subscription.packtpub.com/book/business/9781785283987/1/ch01lvl1sec17/calling-a-mel-script-with-python
.. _Pymel and QT using Designer Noob Question:
   https://discourse.techart.online/t/pymel-and-qt-using-designer-noob-question/1784
.. _Using QT Designer for MEL Interfaces:
   https://www.highend3d.com/maya/tutorials/scripting/mel/c/using-qt-designer-for-mel-interfaces
.. _Maya QT interfaces in a class:
   https://www.chris-g.net/2011/06/24/maya-qt-interfaces-in-a-class/
.. _Using PySide2 to develop Maya Plug-in Series I\: QT Designer to design GUI, pyside-uic to convert. ui file to. py file:
   https://programmer.group/qt-designer-to-design-gui-pyside-uic-to-convert-ui-file-to-py-file.html
.. _TypeError\: 'encoding' is an invalid keyword argument for this function:
   https://stackoverflow.com/questions/12541370/typeerror-encoding-is-an-invalid-keyword-argument-for-this-function#answer-49926118
.. _Building Sphinx documentation for unfriendly code:
   https://www.robg3d.com/2015/01/building-sphinx-documentation-for-unfriendly-code/
.. _Error when autodocumenting pymel code with Sphinx:
   https://discourse.techart.online/t/error-when-autodocumenting-pymel-code-with-sphinx/4972/3
.. _Pyside2 with Qt Designer - Resource(icons) ignored when using QUiLoader():
   https://stackoverflow.com/questions/59062024/pyside2-with-qt-designer-resourceicons-ignored-when-using-quiloader
.. _Thread\: QUiLoader & *.qrc files?:
   https://www.qtcentre.org/threads/57948-QUiLoader-amp-*-qrc-files#post_258528

"""

import os
import sys



import ui_functions


__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"


__all__ = [
    'ScriptName'
]





class DatabaseObject(object):

    def __init__(self, *args, **kwargs):
        super(ScriptName, self).__init__(*args, **kwargs)

        # Loads the window.
        self.widget = QUiLoader().load(UI_FILE)

        # This structure closes the files automatically.
        with io.open(THEME_FILE, "r", encoding='utf-8') as theme, io.open(STYLESHEET_FILE, "r", encoding='utf-8') as style:
            complete_stylesheet = theme.read()
            complete_stylesheet += style.read()
            self.widget.setStyleSheet(complete_stylesheet)

        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.widget.windowTitle())

        # Connects the event (clicked) to the method.
        self.widget.pushButton_3.clicked.connect(self.escreveNome)

    def get_text_from_textbox(self):
        return self.widget.lineEdit.text()

    def escreveNome(self):
        text = self.get_text_from_textbox()
        self.widget.label.setText("Welcome, " + text + ".")


class Bicycle():
