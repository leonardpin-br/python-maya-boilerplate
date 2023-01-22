#! /bin/bash

# This script updates the make.bat file that is used by Sphinx during the
# documentation process.
#
# This file updates the line:
# set SPHINXBUILD=sphinx-build
# Changing it to the full path of the build_sphinx_mayadoc.py file.
#
# This script expects, as an optional argument, the relative path to the file.
# If not provided, it defaults to <project_root>/docs/sphinx/make.bat.
#
# REFERENCES:
# https://www.cyberciti.biz/faq/linux-unix-applesox-bsd-bash-cstyle-for-loop/
# https://stackoverflow.com/questions/11245144/replace-whole-line-containing-a-string-using-sed
# https://stackoverflow.com/questions/12487424/uppercase-first-character-in-a-variable-with-bash

include() {
    # MY_DIR is the <project_root>/scripts directory.
    MY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

    . "${MY_DIR}"/$1
}

# Included files
include "utils.sh"

# Updates the absolute path in the make.bat file.
# param1 (string): The make.bat file. Defaults to ./docs/sphinx/make.bat.
update_make_bat() {

    # Clears the terminal window.
    clear

    # Gives a default value to the parameter.
    local MAKE_BAT="${1:-./docs/sphinx/make.bat}"

    # Verifies the existence of the make.bat file.
    if [ ! -f $MAKE_BAT ]; then
        echo -e "The default expected make.bat file is ./docs/sphinx/make.bat"
        echo -e "If you are not using this make.bat, a path to another one must be provided."
        echo -e "The path is relative to the root project folder, like ./docs/sphinx/another-make.bat."
        exit 1
    fi

    # The root directory:
    local ROOT_DIR=$(get_root_directory)

    # Removes the prefix if necessary.
    ROOT_DIR=$(remove_prefix "${ROOT_DIR}")

    # Establishes the paths to the project folders.
    local RESOURCES_DIR="${ROOT_DIR}/resources"
    local DOCUMENTATION_CONFIG_DIR="${RESOURCES_DIR}/documentation_config"

    # The path to the configuration file.
    local CONFIG_FILE=""

    # Builds the new line.
    CONFIG_FILE="${CONFIG_FILE}\tset SPHINXBUILD=mayapy \"${DOCUMENTATION_CONFIG_DIR}/build_sphinx_mayadoc.py\""

    # The old line:
    local OLD_LINE="set SPHINXBUILD="

    # Removes the old line containing the original command (sphinx-build)
    # and places the new one.
    sed -i "s+.*$OLD_LINE.*+$CONFIG_FILE+" $MAKE_BAT

    # done
    echo -e "The path in the make.bat file was updated."
    exit 0

}

update_make_bat $1