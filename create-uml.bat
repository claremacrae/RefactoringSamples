del /s /q *.puml
del /s /q *.svg
puml-gen RefactoringSamples uml -dir -excludePaths RefactoringSamples\out
plantuml -tsvg uml\*.puml
plantuml -tsvg uml\Extract\*.puml
plantuml -tsvg uml\Extract\Before\*.puml
plantuml -tsvg uml\Keys\*.puml
