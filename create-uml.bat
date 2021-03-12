del /s /q *.puml
del /s /q *.svg
puml-gen RefactoringSamples uml -dir -excludePaths RefactoringSamples\out

plantuml -tsvg "uml\**.puml"
