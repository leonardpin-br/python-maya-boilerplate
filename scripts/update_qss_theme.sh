#!/bin/bash

# REFERENCES:
# https://www.cyberciti.biz/faq/linux-unix-applesox-bsd-bash-cstyle-for-loop/
# https://stackoverflow.com/questions/11245144/replace-whole-line-containing-a-string-using-sed
# https://stackoverflow.com/questions/12487424/uppercase-first-character-in-a-variable-with-bash

# Clear the terminal window.
clear

# Gets the project root directory.
# return (string) The root directory.
get_root_directory() {

    # The directory of this script.
    readonly SCRIPTS_DIR=$(dirname $(readlink -f $0))
    local ROOT_DIR=$(dirname $SCRIPTS_DIR)

    # The return value.
    echo -e "$ROOT_DIR"
}

# Removes Cygwin prefix.
# param1 (string): The root directory path.
removesCygwinPrefix() {

    local ROOT_DIR=$1

    # The Cygwin prefix /cygdrive/e, if exists, must be removed.
    if [[ "$ROOT_DIR" =~ ^\/cygdrive\/[a-z] ]]; then

        # Removes /cygdrive/.
        ROOT_DIR=${ROOT_DIR/\/cygdrive\//}

        # Capitalizes the drive letter (first character).
        ROOT_DIR="${ROOT_DIR^}"

        # Swaps the first / for :/
        ROOT_DIR=${ROOT_DIR/\//\:\/}

    fi

    echo -e "$ROOT_DIR"
}

# Removes Unix prefix.
# param1 (string): The root directory path.
removesUnixPrefix() {

    local ROOT_DIR=$1

    # The Unix prefix /e, if exists, must be removed.
    if [[ "$ROOT_DIR" =~ ^\/[a-z]\/[a-z]+ ]]; then

        # Removes the first /.
        ROOT_DIR=${ROOT_DIR/\//}

        # Capitalizes the drive letter (first character).
        ROOT_DIR="${ROOT_DIR^}"

        # Swaps the (now) first / for :/
        ROOT_DIR=${ROOT_DIR/\//\:\/}

    fi

    echo -e "$ROOT_DIR"
}

# Updates the absolute paths in the theme .qss file.
# param1 (string): The theme file. Defaults to ./resources/qss/Combinear.qss.
updateQssTheme() {

    # Gives a default value to the parameter.
    local THEME="${1:-./resources/qss/Combinear.qss}"

    # Verifies the existence of the theme file.
    if [ ! -f $THEME ]; then
        echo -e "The default expected theme file is ./resources/qss/Combinear.qss"
        echo -e "If not using this theme, another one must be provided."
        echo -e "The path is relative to the root project folder, like ./resources/qss/another-theme.qss."
        exit 1
    fi

    local ROOT_DIR=$(get_root_directory)

    # Discovers the environment this script is running on:
    # https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux
    local environment="$(uname -s)"

    # Checks if a string starts with a value:
    # https://stackoverflow.com/questions/2172352/in-bash-how-can-i-check-if-a-string-begins-with-some-value
    if [[ $environment == CYGWIN* ]]; then
        ROOT_DIR=$(removesCygwinPrefix $ROOT_DIR)
    elif [[ $environment == MINGW* ]]; then
        ROOT_DIR=$(removesUnixPrefix $ROOT_DIR)
    fi

    # Folders
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