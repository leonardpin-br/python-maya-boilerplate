#!/bin/bash

# This script mimics, loosely and in a very crud way, the
# phpunit-skeleton-generator.
#
# This script receives, as argument, the name of the python file that is going
# to be tested.
#
# REFERENCES:
# https://github.com/VitexSoftware/phpunit-skeleton-generator
# https://stackoverflow.com/questions/29713541/recursive-unittest-discover#answer-29715336

include() {
    # MY_DIR corresponds to the folder where this file is.
    MY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    . "${MY_DIR}"/$1
    # ==========================================================================
    # MY_DIR=/home/web/Documents/GitHub/python-maya-boilerplate/scripts
}

# Included files:
include "utils.sh"

# Global variables:
tabs_as_spaces="    "

# Gets the number of levels deep (number of subfolders) the file is in.
# param1 (string): The file relative path.
get_levels_deep() {

    # Back up of IFS.
    # https://stackoverflow.com/a/10586169
    local original_IFS=$IFS

    # Changes IFS and breaks the path into an array.
    IFS='/' read -r -a path_array <<< "$1"

    # Restores IFS.
    IFS=$original_IFS

    # Stores the number of levels the file is below the src_folder.
    local levels_deep=0

    # Loops through array backwards:
    # https://stackoverflow.com/a/13360181
    # https://www.baeldung.com/linux/bash-script-counter#2-using-the-bash-arithmetic-expansion
    for (( idx=${#path_array[@]}-1 ; idx>=0 ; idx-- )) ; do
        if [ "${path_array[idx]}" = "$src_folder" ]; then
            break
        fi
        levels_deep=$(( levels_deep + 1 ))
    done

    echo -e "$levels_deep"

}

# Inserts the header in the given test file.
# param1 (string): The test file full path.
insert_test_header() {

    local this_script=`basename "$0"`
    local this_date=$(date +'%Y-%m-%d')
    local this_time=$(date +"%T")

    local	file_content="# -*- coding: utf-8 -*-\n"
            file_content="${file_content}u'''Generated by ${this_script} on ${this_date} at ${this_time}.\n"
            file_content="${file_content}'''\n"
            file_content="${file_content}import os\n"
            file_content="${file_content}import sys\n"
            file_content="${file_content}import unittest\n"
            file_content="${file_content}import mock\n"
            file_content="${file_content}\n"
            file_content="${file_content}maya_modules = [\n"
            file_content="${file_content}${tabs_as_spaces}'maya',\n"
            file_content="${file_content}${tabs_as_spaces}'maya.app',\n"
            file_content="${file_content}${tabs_as_spaces}'maya.app.general',\n"
            file_content="${file_content}${tabs_as_spaces}'maya.app.general.mayaMixin',\n"
            file_content="${file_content}${tabs_as_spaces}'cmds',\n"
            file_content="${file_content}${tabs_as_spaces}'mel',\n"
            file_content="${file_content}${tabs_as_spaces}'pymel',\n"
            file_content="${file_content}${tabs_as_spaces}'pymel.core'\n"
            file_content="${file_content}${tabs_as_spaces}'MayaQWidgetBaseMixin',\n"
            file_content="${file_content}${tabs_as_spaces}'MayaQWidgetDockableMixin',\n"
            file_content="${file_content}${tabs_as_spaces}'PySide2',\n"
            file_content="${file_content}${tabs_as_spaces}'PySide2.QtUiTools',\n"
            file_content="${file_content}${tabs_as_spaces}'QtWidgets',\n"
            file_content="${file_content}${tabs_as_spaces}'QUiLoader'\n"
            file_content="${file_content}]\n"
            file_content="${file_content}\n"
            file_content="${file_content}# Creates the mocks.\n"
            file_content="${file_content}for mod in maya_modules:\n"
            file_content="${file_content}${tabs_as_spaces}sys.modules[mod] = mock.MagicMock()\n"

    echo -e "$file_content" >> $1

}

# Solves and inserts the import of the modules being tested.
# param1 (string): The test file full path.
# param2 (int): The number of levels deep.
# param3 (string): The module being tested.
insert_test_imports() {

    local this_script=`basename "$0"`
    local test_full_path="$1"
    local levels_deep=$2
    local   module_name="$3"
            module_name=${module_name%".py"}
    local file_relative_path_from_src="$4"
    local insertion="${file_relative_path_from_src}."

    local file_content="# Automatically calculated by ${this_script} to easily import ${3}:\n"
    file_content="${file_content}# Gets the src_dir.\n"

    local tests_dir="os.path.realpath(__file__)"

    # https://stackoverflow.com/a/169517
    for i in $(seq 1 $levels_deep); do
        tests_dir="os.path.dirname(${tests_dir})"
    done

    file_content="${file_content}tests_dir = ${tests_dir}\n"
    file_content="${file_content}root_dir = os.path.dirname(tests_dir)\n"
    file_content="${file_content}src_dir = os.path.join(root_dir, \"src\")\n"
    file_content="${file_content}\n"
    file_content="${file_content}# Adds src_dir to sys.path if it is not already there:\n"
    file_content="${file_content}for path in sys.path:\n"
    file_content="${file_content}${tabs_as_spaces}if path == src_dir:\n"
    file_content="${file_content}${tabs_as_spaces}${tabs_as_spaces}break\n"
    file_content="${file_content}else:\n"
    file_content="${file_content}${tabs_as_spaces}sys.path.append(src_dir)\n"
    file_content="${file_content}\n"
    file_content="${file_content}\n"

    # If the imported module is the main.py:
    if [ $file_relative_path_from_src == "main.py" ]; then
        insertion=${file_relative_path_from_src%".py"}
    else
        insertion=$(sed -e "s|/|\.|" <<< "$insertion")
        insertion=${insertion%".py."}
    fi

    file_content="${file_content}import ${insertion}\n\n"

    echo -e "$file_content" >> $test_full_path

}

# Inserts the class definition.
# param1 (string): The test file full path.
# param2 (string): The module being tested.
# References:
# https://docs.python.org/2.7/library/unittest.html#organizing-test-code
insert_class_definition() {

    local test_full_path="$1"
    local   class_name="$2"
            class_name=${class_name%".py"}
            class_name="${class_name^}"
    local class_definition="class ${class_name}TestCase(unittest.TestCase):"

    local   file_content="${class_definition}\n"
            file_content="${file_content}\n"
            file_content="${file_content}${tabs_as_spaces}def setUp(self):\n"
            file_content="${file_content}${tabs_as_spaces}${tabs_as_spaces}pass\n"
            file_content="${file_content}\n"
            file_content="${file_content}${tabs_as_spaces}def tearDown(self):\n"
            file_content="${file_content}${tabs_as_spaces}${tabs_as_spaces}pass\n"

    echo -e "$file_content" >> $test_full_path

}

# Inserts the methods definitions for the tested file.
# param1 (string): The test file full path.
# param2 (string): The module being tested.
# References:
# https://unix.stackexchange.com/a/251532
# https://unix.stackexchange.com/questions/671374/linux-find-all-occurrences-of-a-certain-pattern-in-a-line-of-a-file
# https://unix.stackexchange.com/questions/146225/find-all-occurrences-in-a-file-with-sed
# https://stackoverflow.com/questions/15650506/how-can-i-print-out-all-lines-of-a-file-containing-a-specific-string-in-unix
# https://ostechnix.com/the-grep-command-tutorial-with-examples-for-beginners/
# https://stackoverflow.com/a/24890830
# https://stackoverflow.com/a/10586169
# https://stackoverflow.com/a/9294015
insert_method_definition() {

    local test_full_path="$1"
    local file_full_path="$2"

    # Back up of IFS.
    local original_IFS=$IFS

    # Changes IFS.
    IFS='\n'

    # Stores all function/method definitions inside an array.

    # If the file has CRLF (Windows end of lines).
    if [[ $(grep -c $'\r' "$file_full_path") -gt 0 ]]; then
        sed "s/$(printf '\r')\$//" "$file_full_path" > "temp_file.txt"
        readarray original_function_definitions < <(grep "def" temp_file.txt)
        rm "temp_file.txt"
    else
        readarray original_function_definitions < <(grep "def" "$file_full_path")
    fi

    # Restores IFS.
    IFS=$original_IFS

    # Gets only the name of the function/method, skipping __init__:
    local function_definitions_as_string=""
    local ignore_pattern="__init__"

    for i in "${original_function_definitions[@]}"; do

        # Removes leading and trailing spaces.
        i=$(trim "$i")

        if grep -q "$ignore_pattern" <<< "$i"; then
            continue
        fi

        # Removes the prefix.
        i=${i#"def "}

        # Removes the suffix.
        i=$(sed -e "s/[(].*$//" <<< "$i")
        function_definitions_as_string+="$i "

    done

    # Expands the string into an array.
    local new_function_definitions=($function_definitions_as_string)

    local file_content=""

    for j in "${new_function_definitions[@]}"; do
        file_content="${file_content}${tabs_as_spaces}# Covers ${j}.\n"
        file_content="${file_content}${tabs_as_spaces}def test_${j}(self):\n"
        file_content="${file_content}${tabs_as_spaces}${tabs_as_spaces}pass\n\n"
    done

    echo -e "$file_content" >> $test_full_path

}

# Fills the test file with code.
# param1 (string): The test file full path.
# param2 (int): The number of levels deep.
# param3 (string): The module being tested.
# param4 (string): The full path of the module being tested.
fill_test_file() {

    local test_full_path="$1"
    local levels_deep="$2"
    local file_to_be_tested="$3"
    local file_full_path="$4"
    local test_folder_full_path="$5"

    insert_test_header $test_full_path

    insert_test_imports $test_full_path $levels_deep $file_to_be_tested $file_relative_path_from_src

    insert_class_definition $test_full_path $file_to_be_tested

    insert_method_definition $test_full_path $file_full_path

}

# Creates an unit test file from the filename given as argument.
# param1 (string): The filename.
unittest_skeleton_generator() {

    # Clear the terminal window.
    clear

    # Receives the ${fileBasename} (filename with extension).
    local file_to_be_tested="$1"

    local src_folder="src"
    local tests_folder="tests"
    local root_dir=$(get_root_directory)
    # ==========================================================================
    # local root_dir=/home/web/Documents/GitHub/python-maya-boilerplate
    local src_folder_full_path="$root_dir/$src_folder"

    # Limits the search to only the src_folder.
    local file_full_path=$(find "$src_folder_full_path" -name "$file_to_be_tested")

    # Verifies if the argument was passed, and if the file exists.
    # https://stackoverflow.com/a/21164441
    if [ -f $file_to_be_tested ]; then
        print_error_message "This script receives, as argument, the name of the python file (with extension) that is going to be tested.\nThe file must be in the src folder or inside a subfolder."
        exit 1
    elif [[ $file_to_be_tested != *\.py ]]; then
        print_error_message "The file must have the \".py\" extension."
        exit 1
    elif [[ ! -f $file_full_path ]]; then
        print_error_message "File (from which the test will be created) not found in the src folder or in its subfolders."
        exit 1
    fi

    # Builds the relative path, removing the first part of the string path:
    # https://stackoverflow.com/a/16623897
    local file_relative_path=${file_full_path#"$root_dir"}  # /src/shared/functions.py

    # Builds the test relative path:
    # https://stackoverflow.com/a/23715370
    local test_relative_path=$(echo "$file_relative_path" | sed -e "s/$src_folder/$tests_folder/")

    # Gets the number of levels deep
    local levels_deep=$(get_levels_deep $file_relative_path)

    # Removes the prefix if necessary.
    root_dir=$(remove_prefix $root_dir)
    # ==========================================================================

    local test_full_path="${root_dir}${test_relative_path}"

    # Removes the suffix
    # https://stackoverflow.com/a/16623897
    local test_folder_full_path=${test_full_path%"$file_to_be_tested"}
    local init_file="${test_folder_full_path}__init__.py"

    # Creates the test folder (and the path to it) if it does not exist.
    # https://stackoverflow.com/a/793867/3768670
    mkdir -p $test_folder_full_path

    # If the __init__.py does not exist, create it.
    if [ ! -f $init_file ]; then
        touch $init_file
    fi

    # If the test file already exists, exit this script.
    if [ -f $test_full_path ]; then
        print_error_message "The test file already exists."
        exit 1
    fi

    # Creates the test file.
    test_full_path="${test_folder_full_path}test_${file_to_be_tested}"
    touch $test_full_path

    # Works the relative path for import in the test.
    local file_relative_path_from_src=${file_relative_path#"/${src_folder}/"}

    fill_test_file $test_full_path $levels_deep $file_to_be_tested $file_full_path $file_relative_path_from_src

    echo -e "The test skeleton file for ${file_to_be_tested} was created successfully."
    exit 0

}

unittest_skeleton_generator $1
# unittest_skeleton_generator functions.py