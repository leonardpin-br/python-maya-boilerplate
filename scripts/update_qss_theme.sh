#!/bin/bash

# This script updates the .qss theme that is used to customize the UI created
# in Autodesk Maya.
# This file updates lines such as this:
# image: url("F:/d_flux/libraries/scripts/Maya/python-maya-boilerplate/resources/img/arrow-down.png");
# To the lines of the system it is in.
# This script expects, as an optional argument, the relative path to the file.
# If not provided, it defaults to Combinear.qss.
#
# REFERENCES:
# https://www.cyberciti.biz/faq/linux-unix-applesox-bsd-bash-cstyle-for-loop/
# https://stackoverflow.com/questions/11245144/replace-whole-line-containing-a-string-using-sed
# https://stackoverflow.com/questions/12487424/uppercase-first-character-in-a-variable-with-bash

include() {
    # MY_DIR corresponde ao diretório do arquivo principal.
    MY_DIR=$(dirname $(readlink -f $0))
    . $MY_DIR/$1
}

# Included files
include "utils.sh"

# Updates the absolute paths in the theme .qss file.
# param1 (string): The theme file. Defaults to ./resources/qss/Combinear.qss.
updateQssTheme() {

    # Clear the terminal window.
    clear

    # Gives a default value to the parameter.
    local THEME="${1:-./resources/qss/Combinear.qss}"

    # Verifies the existence of the theme file.
    if [ ! -f $THEME ]; then
        echo -e "The default expected theme file is ./resources/qss/Combinear.qss"
        echo -e "If you are not using this theme, a path to another one must be provided."
        echo -e "The path is relative to the root project folder, like ./resources/qss/another-theme.qss."
        exit 1
    fi

    local ROOT_DIR=$(get_root_directory)

    # Discovers the environment this script is running on:
    # see   https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux
    local environment="$(uname -s)"

    # Checks if a string starts with a value:
    # see   https://stackoverflow.com/questions/2172352/in-bash-how-can-i-check-if-a-string-begins-with-some-value
    if [[ $environment == CYGWIN* ]]; then
        ROOT_DIR=$(remove_cygwin_prefix $ROOT_DIR)
    elif [[ $environment == MINGW* ]]; then
        ROOT_DIR=$(remove_unix_prefix $ROOT_DIR)
    fi

    # Establishes the paths to the project folders.
    local RESOURCES_DIR="$ROOT_DIR/resources"
    local IMG_DIR="$RESOURCES_DIR/img"

    # Array with the filenames of the images used in the (Combinear.qss) theme.
    local image_files=(
        "arrow-down.png"
        "arrow-left.png"
        "arrow-right.png"
        "arrow-up.png"
        "check.png"
        "tree-closed.png"
        "tree-open.png"
    )

    # Will hold every image path in the file.
    local NEW_FILE_PATH=""

    # Loops through the array searching for each
    # image filename in the theme file.
    for i in "${image_files[@]}"; do

        # Builds the new line.
        NEW_FILE_PATH="    image: url(\"$IMG_DIR/$i\");"

        # Removes the old line containing the image filename
        # and adds the new one.
        sed -i "s+.*$i.*+$NEW_FILE_PATH+" $THEME

    done

    echo -e "The paths in the theme file were updated."
    exit 0

}

updateQssTheme $1