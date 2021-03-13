#!/usr/bin/env bash

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

./add-missing-include-files.py 
./create-uml.sh
./run_markdown_templates.sh