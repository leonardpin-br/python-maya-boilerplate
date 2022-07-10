#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Entry point of this script/app.

Last modified in 2022-06-29

Python version 2.7.11 (Autodesk Maya 2018 and 2020)

This is the file to run from Autodesk Maya. It is advisable to create a shelf
button to run this app from there.

Example:
    How a shelf button can be written::

        # -*- coding: utf-8 -*-
        u'''Maya shelf button for this app to run.

        This is a (Maya) shelf button example to make this code run without conflict
        with the Sphinx's sphinx-apidoc tool.
        '''

        import sys

        module_path = 'E:\\\\cloud\\\\Backup\\\\Libraries\\\\scripts\\\\maya\\\\Boilerplate\\\\boilerplate'

        # Includes the module path in sys.path if it is not already there:
        for path in sys.path:
            if path == module_path:
                break
        else:
            sys.path.insert(0, module_path)

        import main
        reload(main)

Note:
    If unit tests are in place, this is how they can be run::

        python -m unittest discover

Important:
    Sphinx (and its packages) **MUST** be installed in the virtual environment
    in order to avoid import errors.

    Having multiple Python versions on the machine and Sphinx installed in one
    of them, leads to confusion and hard to track bugs.

Note:
    How to generate the requirements.txt::

        pip freeze > requirements.txt

    How to install packages from requirements.txt::

        pip install -r requirements.txt

Note:
    To exclude certain modules from being documented, it is necessary to pass
    them as arguments to ``sphinx-apidoc``::

        sphinx-apidoc --force -o ./docs/sphinx/source ./boilerplate ./boilerplate/databaseobject/db_credentials.py

    The example above is in the **package.json** file as the ``build:source:doc`` script.

References:
    `sphinx-apidoc ignoring some modules/packages`_

    `Coverage.py`_

    `Configuration reference`_

    `Test Code Coverage`_

    `Python Sphinx exclude patterns`_

    `sphinx-apidoc`_

    `Unpacking kwargs`_

.. _sphinx-apidoc ignoring some modules/packages:
   https://chadrick-kwag.net/sphinx-apidoc-ignoring-some-modules-packages/
.. _Coverage.py:
   https://coverage.readthedocs.io/en/6.3.2/#coverage-py
.. _Configuration reference:
   https://coverage.readthedocs.io/en/6.3.2/config.html#configuration-reference
.. _Test Code Coverage:
   https://cpske.github.io/ISP/testing/code-coverage
.. _Python Sphinx exclude patterns:
   https://stackoverflow.com/a/43868129
.. _sphinx-apidoc:
   https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
.. _Unpacking kwargs:
   https://stackoverflow.com/a/28771348


"""

import os
import sys
import re

import shared
import activerecord
from appclasses.access_database import Bicycle, Admin


def untested_function():
    u"""The only reason this function exists is to not be tested.

    This function will appear, in the coverage HTML report, as an untested
    line of code.

    Returns:
        bool: The value is only an example and will not be used.
    """
    return False


def main():
    u"""The main function to execute the entire project/application.
    """

    # Clear the terminal window.
    os.system('cls' if os.name == 'nt' else 'clear')

    # UI CREATION
    # ==========================================================================
    # global myWin  # It is very necessary!

    # try:
    #     myWin.close()
    # except:
    #     pass

    # myWin = maya_ui_template.ScriptName()
    # myWin.show()

    # CREATING CLASS INSTANCES
    # ==========================================================================
    # obj = example_classes.ExampleSubclass()
    # print(obj.return_message())
    # print(obj.greeter())

    # CONNECTING TO A DATABASE
    # ==========================================================================
    # database = databaseobject.ConnectionDB()
    # result = database.query("""SELECT * from bicycles""")
    # print("BRAND: {}".format(result[0]['brand']))

    # escaped_string = database.escape_string("Bob's Overdrive")
    # print(escaped_string)

    # CREATING A BICYCLE INSTANCE
    # ==========================================================================
    # bike = Bicycle(brand='Schwinn', model_make='Cutter', year_make=2016,
    #                category_make='City', color_make='white', description='', gender='Unisex', price=587, weight_kg=18.7, condition_id=4)

    # FIND ALL
    # ==========================================================================
    # bikes = Bicycle.find_all()

    # for bike in bikes:
    #     print(bike.brand)
    #     print(bike.model)
    #     print(bike.year)
    #     print(bike.category)
    #     print(bike.gender)
    #     print(bike.color)
    #     print("{weight_kg} / {weight_lbs}".format(weight_kg=bike.get_weight_kg(), weight_lbs=bike.weight_lbs))
    #     print(bike.condition_id)
    #     print(bike.price)
    #     print("====================================================\n\n")

    # FIND BY ID
    # ==========================================================================
    # bike = Bicycle.find_by_id(2)

    # if bike:
    #     print(bike.name())
    #     print("-------------------------------------------")
    #     print(bike.id)
    #     print(bike.brand)
    #     print(bike.model)
    #     print(bike.year)
    #     print(bike.category)
    #     print(bike.gender)
    #     print(bike.color)
    #     print("{weight_kg} / {weight_lbs}".format(weight_kg=bike.get_weight_kg(), weight_lbs=bike.weight_lbs))
    #     print(bike.condition())
    #     print("${price}".format(price=bike.price))
    # else:
    #     print("The ID was not found.")

    # CREATING A RECORD
    # ==========================================================================
    # bicycle = Bicycle(brand="Schwinn", model="Cutter", year=2016, category="City", color="white",
    #                   gender="Unisex", price=450, weight_kg=18, condition_id=4, description="")
    # bicycle = Bicycle(brand="Mongoose", model="Switchback Sport", year=2015, category="Mountain", color="blue",
    #                   gender="Mens", price=399, weight_kg=24, condition_id=2, description="")
    # kwargs = {
    #     "brand": "Diamondback",
    #     "model": "Bob's Overdrive",
    #     "year": 2016,
    #     "category": "Mountain",
    #     "color": "dark green",
    #     "gender": "Unisex",
    #     "price": 565,
    #     "weight_kg": 23.7,
    #     "condition_id": 3,
    #     "description": ""
    # }
    # kwargs = {
    #     "brand": "Schwinn",
    #     "model": "Sanctuary 7-Speed",
    #     "year": 2016,
    #     "category": "Cruiser",
    #     "color": "purple",
    #     "gender": "Womens",
    #     "price": 190,
    #     "weight_kg": 19.5,
    #     "condition_id": 3,
    #     "description": ""
    # }
    # kwargs = {
    #     "brand": "Junk Bike",
    #     "model": "Delete me",
    #     "year": 1998,
    #     "category": "Road",
    #     "color": "white",
    #     "gender": "Mens",
    #     "price": 2,
    #     "weight_kg": 1,
    #     "condition_id": 3,
    #     "description": ""
    # }

    # bicycle = Bicycle(**kwargs)
    # result = bicycle.save()
    # if result:
    #     print("The new ID is: {id}".format(id=bicycle.id))
    #     print("The bicycle was created successfully.")
    # else:
    #     print(shared.display_errors(bicycle.errors))

    # UPDATING A RECORD
    # ==========================================================================
    # bike = Bicycle.find_by_id(39)

    # if bike:

    #     kwargs = {
    #         "id": bike.id,
    #         "brand": 'Junk Bike', # bike.brand
    #         "model": bike.model, # Bob's Overdrive
    #         "year": bike.year,
    #         "category": bike.category,
    #         "gender": bike.gender,
    #         "color": bike.color,
    #         "weight_kg": bike.weight_kg,
    #         "condition": bike.condition,
    #         "price": bike.price
    #     }

    #     bike.merge_attributes(**kwargs)
    #     result = bike.save()
    #     if result:
    #         print("The bicycle was updated successfully.")
    #     else:
    #         print(shared.display_errors(bike.errors))
    # else:
    #     print("The ID was not found.")

    # DELETING A RECORD
    # ==========================================================================
    # bike = Bicycle.find_by_id(380)

    # if bike:

    #     result = bike.delete()
    #     if result:
    #         print("{name} was deleted successfully.".format(name=bike.name()))
    #     else:
    #         print("There was an error deleting the bicycle.")

    # else:
    #     print("The ID was not found.")

    # ADMIN FIND ALL
    # ==========================================================================
    # admins = Admin.find_all()

    # for admin in admins:
    #     print(admin.first_name)
    #     print(admin.last_name)
    #     print(admin.email)
    #     print(admin.username)
    #     print("====================================================\n\n")

    # ADMIN FIND BY ID
    # ==========================================================================
    # admin = Admin.find_by_id(1)

    # if admin:
    #     print(admin.full_name())
    #     print("-------------------------------------------")
    #     print(admin.first_name)
    #     print(admin.last_name)
    #     print(admin.email)
    #     print(admin.username)
    # else:
    #     print("The ID was not found.")


    # ADMIN CREATING A RECORD
    # ==========================================================================
    # kwargs = {
    #     "first_name": "Bob",
    #     "last_name": "Smith",
    #     "email": "b@b.com",
    #     "username": "bobsmith",
    #     "password": "Password#1234",
    #     "confirm_password": "Password#1234"
    # }

    # admin = Admin(**kwargs)
    # result = admin.save()
    # if result:
    #     print("The ID of the new admin is: {id}".format(id=admin.id))
    #     print("The admin was created successfully.")
    # else:
    #     print(shared.display_errors(admin.errors))

    # ADMIN UPDATING A RECORD
    # ==========================================================================
    # admin = Admin.find_by_id(12)

    # if admin:

    #     kwargs = {
    #         "first_name": admin.first_name,
    #         "last_name": admin.last_name,
    #         "email": admin.email,
    #         "username": admin.username,
    #         "password": "Password#1234",
    #         "confirm_password": "Password#1234"
    #     }

    #     admin.merge_attributes(**kwargs)
    #     result = admin.save()
    #     if result:
    #         print("The admin was updated successfully.")
    #     else:
    #         print(shared.display_errors(admin.errors))
    # else:
    #     print("The admin ID was not found.")

    # ADMIN PASSWORD VERIFY
    # ==========================================================================
    username = "bobsmith"
    password = "Password#1234"
    admin = Admin.find_by_username(username)

    if admin and admin.verify_password(password):
        print("The given password match with the one stored in the database.")
    else:
        print("The admin password does not match with the original.")


main()
