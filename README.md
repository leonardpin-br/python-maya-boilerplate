# Python starter project to create applications (not only but specially) for Autodesk Maya.

This starter kit is preconfigured to facilitate fast development.

## Inspirations and reference
This kit is heavily influenced by the greate course
[PHP: Object-Oriented Programming with Databases](https://www.linkedin.com/learning/php-object-oriented-programming-with-databases)
taught by Kevin Skoglund. If you are learning about OOP, I highly recommend it
even if PHP is not your primary focus.

## Why is it better than a script in a single file?
This starter kit allows the development of a more powerfull tool. Instead of creating a single script, the user of this kit will be able to create a small application.

## It includes
    1. Easy password hashing and verification (bcrypt). Even though Autodesk Maya is not able to load
    the BCrypt package, if the user of this kit needs to hash and verify a password, it is already
    preconfigured.
    2. An abstract class to be inherited by all the others that access
    the database. It is an application of the __active record__ design pattern.
    3. Two example subclasses are provided. One for a product and one for
    an admin, both are subclasses of the database one (active record).
    4. The code is heavly documented (using Sphinx and Google style docstrings) and HTML generation
    is preconfigured.
    5. General and validation functions that can be easily reused in other
    projects.
    6. Unit tests and coverage are preconfigured.

## Dependencies
It depends on Node.js, but only for development (documentation and unit tests).

Having a MySQL database server is only necessary if you need communication with
one. If your scripts do not access a database, you do not need it.

If you use a Database Management System (DBMS) different from MySQL, editing the code will be easy.

It is important to install the correct Python version (2.7.11 for Maya 2020 and below)
in the operating system and to create a virtual environment (py27env folder).

After that, it is important to install the necessary packages (inside the virtual
environment) using:
```
pip install -r requirements.txt
```

## Folder structure
```
<project_root>
|- src                  (the app)
    |- activerecord     (modules that implement the active record design pattern)
    |- appclasses       (classes specific for the application being developed)
    |- shared           (usefull functions shared by the packages)
    |- userinterface    (example of user interface class and related modules)
|- docs                 (for the generated HTML documentation and coverage reports)
    |- coverage         (for the generated HTML code coverage reports)
    |- sphinx           (for the generated HTML documentation)
|- py27env              (virtual environment folder)
|- resources            (good to have and needed files)
    |- example_files    (files that can be used as reference)
    |- img              (images used in the interface creation)
    |- qss              (for interface customization)
    |- sql              (for databases)
    |- ui               (files created in Qt Designer)
|- scripts              (usefull bash scripts)
|- tests                (unit tests)

```

## Which file will be executed?
Using this starter kit, the main.py (``<project_root>/src/main.py``) will be
the file being executed from Autodesk Maya.

It is recommended to create a shelf button that imports the main.py file (there is
an example in the ``resources/example_files`` folder).

