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

# Prints an error message that is easy to read in the console.
# param1 (string): The error message to be printed.
print_error_message() {
    echo -e "\n--------------------------------------------------------------\n"
    echo -e "$1"
    echo -e "\n--------------------------------------------------------------\n\n"
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

# Removes the environment (MINGW, Cygwin...) from the string path.
# param1 (string): The root directory path.
remove_prefix() {

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

    echo -e "$root_dir"

}

# Trims the begining of the given string.
# param1 (string): The string to be trimmed.
# https://stackoverflow.com/a/3232433
remove_leading_whitespace_only() {
    local no_lead_whitespace="$(echo -e "${1}" | sed -e 's/^[[:space:]]*//')"
    echo -e "$no_lead_whitespace"
}

# Trims the end of the given string.
# param1 (string): The string to be trimmed.
# https://stackoverflow.com/a/3232433
remove_trailing_whitespace_only() {
    local no_trail_whitespace="$(echo -e "${1}" | sed -e 's/[[:space:]]*$//')"
    echo -e "$no_trail_whitespace"
}

# Trims a given string.
# param1 (string): The string to be trimmed.
# https://stackoverflow.com/a/3232433
trim() {
    local   result="$(echo -e "${1}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
    echo "$result"
}