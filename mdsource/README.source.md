<a id="top"></a>

# RefactoringSamples

toc

## Purpose

To provide visualisations of micro-refactorings in C# code, using UML diagrams generated from pairs of tiny C# source files.

## Refactoring Samples

### Key

![Key](uml/Keys/Key.svg?raw=true)

### Extract Refactorings

#### Extract Field

include: ExtractField

#### Extract Field with Static members

include: ExtractFieldStatic

#### Extract Class

include: ExtractClass

#### Extract Superclass

include: ExtractSuperclass

#### Extract Interface

include: ExtractInterface

### Encapsulate Refactorings

#### Encapsulate Field

include: EncapsulateField

## Creating a new pair of files

1. Create a new .cs file in a sub-dir of `RefactoringSamples/Before`
1. Set it up with the methods and fields that you want to demo
1. Make sure its namespace matches its location
1. Select the class name and Refactor This and Copy Type
    * Change the namespace from Before to After
1. In the new file, apply the refactoring
1. Run `create-uml.bat`
1. Add the new files to README.md
1. Review and commit the files

## Reference

* "Refactoring: Improving the Design of Existing Code", Second Edition by Martin Fowler
  * [The Second Edition of "Refactoring"](https://martinfowler.com/articles/refactoring-2nd-ed.html)
  * [Accessing the web edition of Refactoring](https://martinfowler.com/articles/access-refactoring-web-edition.html)
  * [Online Catalog of Refactorings](https://refactoring.com/catalog/)
* [JetBrains Rider Refactorings](https://www.jetbrains.com/help/rider/Refactorings__Index.html)

## Ideas

* Machine-generate markdown pages that show the Before and After of both the .cs source and the .svg files.
* Try generating combined .svg files that show the Before and After UML, with an arrow between the two.
* Add this to readthedocs
