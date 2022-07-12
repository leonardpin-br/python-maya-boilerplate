#!/bin/bash

# https://askubuntu.com/questions/153144/how-can-i-recursively-search-for-directory-names-with-a-particular-string-where
# https://www.cyberciti.biz/faq/how-to-find-and-delete-directory-recursively-on-linux-or-unix-like-system/
# https://stackoverflow.com/questions/2135770/bash-for-loop-with-wildcards-and-hidden-files

clear_cache() {

    # Clear the terminal window.
    clear

    local __PYCACHE__="__pycache__"
    local PYC="*.pyc"

    # Delete all __pycache__ folders recursively from the root directory.
    find ./ -type d -name "${__PYCACHE__}" -exec rm -rf {} +

    # Delete all .pyc files recursively from the root directory.
    find ./ -type f -name "${PYC}" -exec rm -rf {} +

    echo -e "Cache cleared."
    # exit 0

}

# clear_cache