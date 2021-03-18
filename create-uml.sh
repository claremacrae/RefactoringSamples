#!/usr/bin/env bash

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

# https://github.com/pierre3/PlantUmlClassDiagramGenerator
# Option -createAssociation looked like it would be useful, but for
# ExtractClass.svg, the layout was terrible, with _concept2 overlapping
# the Concept2 class
puml-gen RefactoringSamples uml -dir -excludePaths RefactoringSamples\out

# Delete a file which gives an error on Mac:
#   Error line 2 in file: uml/include.puml
#   Some diagram description contains errors
rm uml/include.puml

plantuml -tsvg 'uml/**.puml'
