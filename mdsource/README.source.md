<a id="top"></a>

# RefactoringSamples

toc

## Purpose

To provide visualisations of micro-refactorings in C# code, using UML diagrams generated from pairs of tiny C# source files.

## Key

![Key](uml/Keys/FullKey.svg?raw=true)

## The Refactorings

See the [List of Refactorings](docs/README.md#top).

## Tools Used

* Hirotada Kobayashi's [PlantUmlClassDiagramGenerator](https://github.com/pierre3/PlantUmlClassDiagramGenerator)
* [PlantUML](https://plantuml.com)
* SimonCropp's [MarkdownSnippets](https://github.com/SimonCropp/MarkdownSnippets)

## Appendix

### Creating a new pair of files

1. Create a new .cs file in a sub-dir of `RefactoringSamples/Before`
1. Set it up with the methods and fields that you want to demo
1. Make sure its namespace matches its location
1. Select the class name and Refactor This and Copy Type
    * Change the namespace from Before to After
    * Move the new file to the correct location inside `RefactoringSamples/After`
1. In the new file, apply the refactoring
1. Add new heading and `include:` line to `mdsource/README.source.md`
1. Run `update-docs.sh`
1. Review and commit the files

### Ideas

* Machine-generate markdown pages that show the Before and After of both the .cs source and the .svg files.
* Try generating combined .svg files that show the Before and After UML, with an arrow between the two.
* Add this to readthedocs
