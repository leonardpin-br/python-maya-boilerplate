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
    local root_dir=$(get_root_directory)
    local application_folder="$root_dir/$app_folder"
    local file_full_path=$(find "$application_folder" -name "$file_to_be_tested")

    # Verifies if the argument was passed, and if the file exists.
    # https://stackoverflow.com/a/21164441
    if [ -f $file_to_be_tested ]; then
        echo -e "This script receives, as argument, the name of the python file (with extension) that is going to be tested."
        exit 1
    elif [[ ! -f $file_full_path ]]; then
        echo -e "File not found."
        exit 1
    fi

    # Builds the full file path to the file that is going to be tested.
    # local file_relative_folder=$(get_file_relative_folder "$file_to_be_tested")
    # # local file_full_folder_path=$(realpath $file_relative_folder)
    # # local file_full_path="${file_full_folder_path}/${file_to_be_tested}"

    # --------------------------------------------------------
    # Levels:
    # boilerplate           0
    # main.py               1
    # shared/functions.py   2
    # --------------------------------------------------------




    # # Creates the full folder path for the test file that will be created.
    # local tests_full_folder_path="${root_dir}/tests"
    # # local tests_full_folder_path=${file_full_folder_path/src/"$tests_replacement"}


    # echo -e "$tests_full_folder_path"

    # # Discovers the environment this script is running on:
    # # see   https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux
    # local environment="$(uname -s)"

    # # Checks if a string starts with a value:
    # # see   https://stackoverflow.com/questions/2172352/in-bash-how-can-i-check-if-a-string-begins-with-some-value
    # if [[ $environment == CYGWIN* ]]; then
    #     root_dir=$(remove_cygwin_prefix $root_dir)
    # elif [[ $environment == MINGW* ]]; then
    #     root_dir=$(remove_unix_prefix $root_dir)
    # fi

    # # Establishes the paths to the project folders.
    # local RESOURCES_DIR="$root_dir/resources"
    # local IMG_DIR="$RESOURCES_DIR/img"

    # # Array with the filenames of the images used in the (Combinear.qss) theme.
    # local image_files=(
    #     "arrow-down.png"
    #     "arrow-left.png"
    #     "arrow-right.png"
    #     "arrow-up.png"
    #     "check.png"
    #     "tree-closed.png"
    #     "tree-open.png"
    # )

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

unittest_skeleton_generator $1