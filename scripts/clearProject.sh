#!/bin/bash

# https://askubuntu.com/questions/153144/how-can-i-recursively-search-for-directory-names-with-a-particular-string-where
# https://www.cyberciti.biz/faq/how-to-find-and-delete-directory-recursively-on-linux-or-unix-like-system/
# https://stackoverflow.com/questions/2135770/bash-for-loop-with-wildcards-and-hidden-files

clearProject() {

    # Clear the terminal window.
    clear

    # Folders
    local DOCS="./docs"

    local COVERAGE="$DOCS/coverage"
    local HTMLCOV="$COVERAGE/htmlcov"

    local SPHINX="$DOCS/sphinx"
    local BUILD="$SPHINX/build"
    local SOURCE="$SPHINX/source"
    local _STATIC="$SOURCE/_static"
    local _TEMPLATES="$SOURCE/_templates"

    local NODE_MODULES="./node_modules"
    local __PYCACHE__="__pycache__"
    local PYC="*.pyc"

    # Files
    local GITIGNORE="$HTMLCOV/.gitignore"
    local DOT_COVERAGE="$COVERAGE/.coverage"

    local MAKE_BAT="$SPHINX/make.bat"
    local MAKEFILE="$SPHINX/Makefile"
    local CONF_PY="$SOURCE/conf.py"
    local INDEX_RST="$SOURCE/index.rst"

    # Works the ./docs folder.
    for item in "$DOCS"/*; do

        # Works the ./docs/coverage folder.
        if [ $item = $COVERAGE ]; then

            # Enable working with hidden files.
            shopt -s dotglob
            for coverageItem in "$COVERAGE"/*; do

                # Clear folder ./docs/coverage/htmlcov
                if [ $coverageItem = $HTMLCOV ]; then
                    rm -rf "$HTMLCOV"/*

                    # Clear the hidden file (.gitignore)
                    if [ -f $GITIGNORE ]; then
                        rm -f "$GITIGNORE"
                    fi

                # If it is .coverage (data file)
                elif [ $coverageItem = $DOT_COVERAGE ]; then
                    rm -f "$DOT_COVERAGE"

                # Remove everything else inside ./docs/coverage.
                else
                    rm -f $coverageItem
                fi

            done
            # Disable working with hidden files.
            shopt -u dotglob

        # Works the ./docs/sphinx folder.
        elif [ $item = $SPHINX ]; then

            for sphinxItem in "$SPHINX"/*; do

                # Clear folder ./docs/sphinx/build
                if [ $sphinxItem = $BUILD ]; then
                    rm -rf "$BUILD"/*

                # Works the ./docs/sphinx/source folder.
                elif [ $sphinxItem = $SOURCE ]; then

                    for sourceItem in "$SOURCE"/*; do

                        # Clear folder ./docs/sphinx/source/_static
                        if [ $sourceItem = $_STATIC ]; then
                            rm -rf "$_STATIC"/*

                        # Clear folder ./docs/sphinx/source/_templates
                        elif [ $sourceItem = $_TEMPLATES ]; then
                            rm -rf "$_TEMPLATES"/*

                        # If it is ./docs/sphinx/source/conf.py
                        elif [ $sourceItem = $CONF_PY ]; then
                            continue

                        # If it is ./docs/sphinx/source/index.rst
                        elif [ $sourceItem = $INDEX_RST ]; then
                            continue

                        # Removes everything else inside ./docs/sphinx/source.
                        else
                            rm -f $sourceItem
                        fi

                    done

                # If it is ./docs/sphinx/make.bat
                elif [ $sphinxItem = $MAKE_BAT ]; then
                    continue

                # If it is ./docs/sphinx/Makefile
                elif [ $sphinxItem = $MAKEFILE ]; then
                    continue

                # Remove everything else inside ./docs/sphinx su
                else
                    rm -f $sphinxItem
                fi

            done

        # Remove everything outside ./docs/coverage and ./docs/sphinx subfolders.
        else
            rm -f $item
        fi

    done

    # Remove folder ./node_modules
    if [ -d $NODE_MODULES ]; then
        rm -rf "$NODE_MODULES"
    fi

    # Delete all __pycache__ folders recursively from the root directory.
    find ../ -type d -name "$__PYCACHE__" -exec rm -rf {} +

    # Delete all .pyc files recursively from the root directory.
    find ../ -type f -name "$PYC" -exec rm -rf {} +

    echo -e "Project cleared."
    exit 0

}

clearProject