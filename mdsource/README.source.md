<a id="top"></a>

# RefactoringSamples

toc

## Purpose

To provide visualisations of micro-refactorings in C# code, using UML diagrams generated from pairs of tiny C# source files.

## Key

![Key](uml/Keys/FullKey.svg?raw=true)

## The Refactorings

See the [List of Refactorings](docs/README.md#top).

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

### Reference

* "Refactoring: Improving the Design of Existing Code", Second Edition by Martin Fowler
  * [The Second Edition of "Refactoring"](https://martinfowler.com/articles/refactoring-2nd-ed.html)
  * [Accessing the web edition of Refactoring](https://martinfowler.com/articles/access-refactoring-web-edition.html)
  * [Online Catalog of Refactorings](https://refactoring.com/catalog/)
* [JetBrains Rider Refactorings](https://www.jetbrains.com/help/rider/Refactorings__Index.html)

### Ideas

* Machine-generate markdown pages that show the Before and After of both the .cs source and the .svg files.
* Try generating combined .svg files that show the Before and After UML, with an arrow between the two.
* Add this to readthedocs
