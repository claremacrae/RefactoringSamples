#!/usr/bin/env bash

# Force execution to halt if there are any errors in this script:
#set -e
#set -o pipefail

find . \( -name \*.puml -o -name \*.svg \) -exec rm {} \;
puml-gen RefactoringSamples uml -dir -excludePaths RefactoringSamples\out | grep -v "^Processing "

# Delete a file which gives an error on Mac:
#   Error line 2 in file: uml/include.puml
#   Some diagram description contains errors
rm uml/include.puml

plantuml -tsvg 'uml/**.puml'
