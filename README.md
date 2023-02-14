# Python starter project to create applications (not only but specially) for Autodesk Maya.

This starter kit is preconfigured to facilitate fast development.



## Before you begin

### Git and Cygwin
Install Git (and Git Bash) for version control.

Cygwin is a good terminal and I suggest you use it. But, you can execute the BASH
scripts with just Git Bash.

### Spaces in file paths
Make sure you clone this repository to a path without spaces in it. Maya can and do execute without problems, but Sphinx will throw an error if there are any spaces in the path.

### _example files
There are files that have ``_example`` in their names. Those files were created to deal with source control.

It is necessary to copy and rename them, removing the ``_example``. Those files are:

```
<project_root>/.vscode/settings_example.json
<project_root>/docs/sphinx/make_example.bat
<project_root>/resources/qss/Combinear_example.qss
```

### Line endings (CRLF and LF) on Windows
The ``<project_root>/docs/sphinx/make.bat`` file should have CRLF line endings.

The BASH script (``.sh``) files should have LF (Unix) line endings even if you are using Windows. They should be executed in Cygwin or Git Bash.

The provided ``.gitattributes`` file has a configuration that should work without problems (Reference: [Configuring Git to handle line endings](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)).



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
    the database. It is an application of the active record design pattern.
    3. Two example subclasses are provided. One for a product and one for
    an admin, both are subclasses of the database one (active record).
    4. The code is heavly documented (using Sphinx and Google style docstrings) and HTML generation
    is preconfigured.
    5. General and validation functions that can be easily reused in other projects.
    6. Unit tests and coverage are preconfigured.
    7. Line endings are preconfigured.



## Dependencies

### Node.js
It depends on Node.js, but only for development (documentation and unit tests).

Install Node.js and navigate to the root folder of this project. Install node
dependencies with the command:

```
npm install
```

The provided `package.json` file has many useful scripts.

### MySQL

Having a MySQL database server is only necessary if you need communication with
one. If your scripts do not access a database, you do not need it.

If you use a Database Management System (DBMS) different from MySQL, editing the
code will be easy.

### Python version and virtual environments

It will be advantageous to install a Python 3 version first and them install the
`virtualenv` package. One advantage of having Python 3 is the possibility to
install tools like Qt Designer later. Another very useful factor is the
installation of lauchers. The configuration os Sphinx will depend on it later.

`virtualenv` will allow you to create virtual environments.

You could do it with only one (Python 2) version
(Reference: [Create virtualenv in Python 2.7 on windows 10 while other virtualenv are working in Python 3.8](https://stackoverflow.com/a/64940580/3768670))
if you wanted. But, I do not recommend it.

The command to install the recommended package is:

```
pip install virtualenv
```

After that, install the correct version (2.7.11 for Maya 2020)
in the operating system.

Then, create a virtual environment (`py27env` folder)
in the root folder of this project. Run this command from the project's root folder:

```
virtualenv --python="C:/Program Files/Python27/python.exe" "./py27env"
```

Activate the virtual environment with the command:
```
source ./py27env/Scripts/activate   => Cygwin and Git Bash
py27env\Scripts\activate            => Command Prompt
py27env\Scripts\activate.ps1        => PowerShell
```

It is important to install the necessary packages using the command below from
the project's root:
```
pip install -r requirements.txt
```
It will install all the packages, including the appropriate version of Sphinx.



## Documentation
By now, you should have installed Sphinx inside the virtual environment (`py27env` folder).

### Terminals on Windows systems
On Windows systems, the terminal you are using makes a big difference. On my tests, I used
- Command Prompt
- Cygwin
- Git Bash
- Powershell

Even after activating the virtual environment in all of them, the results may differ.

### The shebang line

Only the files that are intended to be executed directly should have the shebang line (Reference: [3.7 Shebang Line](https://google.github.io/styleguide/pyguide.html#37-shebang-line)). In this code, there are only two files that should have it:
```
<project_root>/src/main.py
<project_root>/resources/documentation_config/build_sphinx_mayadoc.py
```

Windows do not support the shebang line (the first line starting with `#! `). But, since Python 3.3 (Reference: [Should I put #! (shebang) in Python scripts, and what form should it take?](https://stackoverflow.com/a/14599026/3768670)), Python installs launchers like

```
"C:\Windows\pyw.exe"
```

The `.py` files should be associated with the above laucher as the default program to execute them.

___________

In my tests, **the shebang line only makes a difference if the main script file is executed directly.** That is what will be discussed below.

___________

#### The tested shebang lines

The laucher **does read** the shebang lines. The commands for each terminal are:
```
code/python/src/main.py       => Cygwin and Git Bash
code\python\src\main.py       => Command Prompt
.\code\python\src\main.py     => PowerShell
```

The result is:

```
#! mayapy.exe                                           => Cygwin only accepts this one.
#! /c/Progra~1/Autodesk/Maya2020/bin/mayapy.exe         => Git Bash accepts the first and the second.
#! "C:\Program Files\Autodesk\Maya2020\bin\mayapy.exe"  => Only accepted by Command Prompt and PowerShell.
```

The only shebang line that worked in all of the tested terminals was `#! mayapy.exe`. That line depends on the alteration of the system environment variables. The steps are listed below.

### Step-by-step on Windows systems
For the documentation generation to work as expected, it is necessary to do the following:

#### 1. Edit the environment variables
Add the path to the `mayapy.exe` to the system variables. The default path is
```
C:\Program Files\Autodesk\Maya2020\bin
```
Move it tho the top of the list.

#### 2. Edit the make.bat file
Make a copy of `<project_root>/docs/sphinx/make.bat.dist` and rename the copy to `make.bat`. This is necessary because of Git source control.

Sphinx will be configured to use the Maya interpreter (`mayapy.exe`) instead of the interpreter in the virtual environment.

`sphinx-quickstart` creates two important files (they are inside the `<project_root>/docs/sphinx` folder):

```
make.bat    => Edit this one if you are on Windows.
Makefile
```

There is a script in the `package.json` file to make it easy. Just run this command
in a terminal like **Cygwin** or **Git Bash**:

```
npm run update:make_bat
```

It executes a BASH script (`<project_root>/scripts/update_make_bat.sh`). In turn, that script edits the `make.bat` file with the follwing:

```
set SPHINXBUILD=mayapy "full/path/to/the/build_sphinx_mayadoc.py"
```

The `mayapy` command is important. Without it, all terminals fail to generate the documentation.

The `"C:/Windows/pyw.exe"` command would also work, but it is inconvenient because it keeps opening and closing other windows while executing. When it finishes, it closes and it is not possible
to see any enventual error. So, it should not be used.

The above file (`build_sphinx_mayadoc.py`) is a custom config file that instructs Sphinx to work with the Maya modules.

#### Portability

In Windows (inside `make.bat`), the path with foward slashes (`/`) works as well as with back slashes (`\`). To keep it easy to copy and paste between different systems, it is best to keep the `/`.

Also to keep this code more portable, the shebang line inside `build_sphinx_mayadoc.py` was set to `#! /usr/bin/env mayapy`.

___________

**With the `mayapy` command in `make.bat`, the shebang line (`#! mayapy.exe` or `#! /usr/bin/env mayapy`) inside `build_sphinx_mayadoc.py` makes absolutely no difference. It works with or without it.**

With the `"C:/Windows/pyw.exe"` command, the shebang line (`#! mayapy.exe`) is probably read, but it's not advisable to use it as stated above.

___________

#### If the Makefile is edited instead of the make.bat

The result is the same on all terminals:

- The Python executable is the one inside the py27env.

- That interpreter does not know anything about any Maya module. So, it fails to import them.



## Folder structure
```
<project_root>
|- src                          (the app)
    |- activerecord             (modules that implement the active record design pattern)
    |- appclasses               (classes specific for the application being developed)
    |- shared                   (usefull functions shared by the packages)
    |- userinterface            (example of user interface class and related modules)
|- docs                         (for the generated HTML documentation and coverage reports)
    |- coverage                 (for the generated HTML code coverage reports)
    |- sphinx                   (for the generated HTML documentation)
|- py27env                      (virtual environment folder)
|- resources                    (good to have and needed files)
    |- documentation_config     (configuration for Sphinx)
    |- example_files            (files that can be used as reference)
    |- img                      (images used in the interface creation)
    |- qss                      (for interface customization)
    |- sql                      (for databases)
    |- ui                       (files created in Qt Designer)
|- scripts                      (usefull bash scripts)
|- tests                        (unit tests)

```



## Which file will be executed?
Using this starter kit, the main.py (``<project_root>/src/main.py``) will be
the file being executed from Autodesk Maya.

It is recommended to create a shelf button that imports the main.py file (there is
an example in the ``resources/example_files`` folder).

