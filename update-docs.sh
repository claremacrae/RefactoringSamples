#!/usr/bin/env bash

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

# TODO Fix failure to find scripts module
# Traceback (most recent call last):
#  File "./create-pattern.py", line 5, in <module>
#    from scripts.constants import do_not_overwrite, overwrite_if_exists
#ModuleNotFoundError: No module named 'scripts'
#cd  scripts
#./create-pattern.py
#cd ..

./create-uml.sh
./run_markdown_templates.sh