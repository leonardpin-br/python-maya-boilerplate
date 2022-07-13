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