#!/usr/bin/env sh

find . -name \*.puml -o -name \*.svg -exec rm {} \;
puml-gen RefactoringSamples uml -dir -excludePaths RefactoringSamples\out

plantuml -tsvg 'uml/**.puml'
