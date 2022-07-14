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
    MY_DIR=$(dirname $(readlink -f $0))
    . $MY_DIR/$1
}

# Included files
include "utils.sh"

# Creates an unit test file from the filename given as argument.
# param1 (string): The filename.
unittest_skeleton_generator() {

    # Clear the terminal window.
    clear

    # Receives the ${fileBasename} (filename with extension).
    local file_to_be_tested="$1"

    local app_folder="boilerplate"
    local tests_folder="tests"
    local root_dir=$(get_root_directory)
    local app_folder_full_path="$root_dir/$app_folder"
    local tests_folder_full_path="$root_dir/$tests_folder"
    local file_full_path=$(find "$app_folder_full_path" -name "$file_to_be_tested")

    # Verifies if the argument was passed, and if the file exists.
    # https://stackoverflow.com/a/21164441
    if [ -f $file_to_be_tested ]; then
        echo -e "This script receives, as argument, the name of the python file (with extension) that is going to be tested."
        exit 1
    elif [[ ! -f $file_full_path ]]; then
        echo -e "File not found."
        exit 1
    fi

    # Builds the relative path, removing the first part of the string path:
    # https://stackoverflow.com/a/16623897
    local file_relative_path=${file_full_path#"$root_dir"}  # /boilerplate/shared/functions.py

    # Builds the test relative path:
    # https://stackoverflow.com/a/23715370
    local test_relative_path=$(echo "$file_relative_path" | sed -e "s/$app_folder/$tests_folder/")

    # Back up of IFS.
    # https://stackoverflow.com/a/10586169
    local original_IFS=$IFS

    # Changes IFS and breaks the path into an array.
    IFS='/' read -r -a path_array <<< "$file_relative_path"

    # Restores IFS.
    IFS=$original_IFS

    # Stores the number of levels the file is below the app_folder.
    local levels_deep=0

    # Loops through array backwards:
    # https://stackoverflow.com/a/13360181
    # https://www.baeldung.com/linux/bash-script-counter#2-using-the-bash-arithmetic-expansion
    for (( idx=${#path_array[@]}-1 ; idx>=0 ; idx-- )) ; do
        if [ "${path_array[idx]}" = "$app_folder" ]; then
            break
        fi
        levels_deep=$(( levels_deep + 1 ))
    done

    # Discovers the environment this script is running on:
    # see   https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux
    local environment="$(uname -s)"

    # Checks if a string starts with a value:
    # see   https://stackoverflow.com/questions/2172352/in-bash-how-can-i-check-if-a-string-begins-with-some-value
    if [[ $environment == CYGWIN* ]]; then
        root_dir=$(remove_cygwin_prefix $root_dir)
    elif [[ $environment == MINGW* ]]; then
        root_dir=$(remove_unix_prefix $root_dir)
    fi

    # TODO:
    # If test folder does not exist, create it.
    # Create the test file
    # Work the content of the file using levels deep
    # Refactor the remove prefix for a function in utils.sh
    echo -e "Test"

    # # Will hold every image path in the file.
    # local NEW_FILE_PATH=""

    # # Loops through the array searching for each
    # # image filename in the theme file.
    # for i in "${image_files[@]}"; do

    #     # Builds the new line.
    #     NEW_FILE_PATH="    image: url(\"$IMG_DIR/$i\");"

    #     # Removes the old line containing the image filename
    #     # and adds the new one.
    #     sed -i "s+.*$i.*+$NEW_FILE_PATH+" $THEME

    # done

    # echo -e "The paths in the theme file were updated."
    # exit 0

}

# unittest_skeleton_generator $1
unittest_skeleton_generator "functions.py"