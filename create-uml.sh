#!/usr/bin/env sh

find . -name \*.puml -o -name \*.svg -exec rm {} \;
puml-gen RefactoringSamples uml -dir -excludePaths RefactoringSamples\out | grep -v "^Processing "

plantuml -tsvg 'uml/**.puml'
