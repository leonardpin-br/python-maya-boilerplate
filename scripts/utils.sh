#!/bin/bash

# Gets the project root directory.
# return (string) The root directory.
get_root_directory() {

    # The directory of this script.
    readonly SCRIPTS_DIR=$(dirname $(readlink -f $0))
    local ROOT_DIR=$(dirname $SCRIPTS_DIR)

    # The return value.
    echo -e "$ROOT_DIR"
}

# param1 (string): The filename with extension.
get_file_relative_folder() {
    local file_relative_folder=$(find . -name "$1" -printf '%h\n')
    echo "$file_relative_folder"
}

# Removes Cygwin prefix.
# param1 (string): The root directory path.
remove_cygwin_prefix() {

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
remove_unix_prefix() {

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