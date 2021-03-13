<a id="top"></a>

# RefactoringSamples

toc

## Purpose

To provide visualisations of micro-refactorings in C# code, using UML diagrams generated from pairs of tiny C# source files.

## Refactoring Samples

### Key

![ExtractField - Before](uml/Keys/Key.svg?raw=true)

### Extract Refactorings

#### Extract Field

![ExtractField - Before](uml/Before/Extract/ExtractField.svg?raw=true)

becomes

![ExtractField - After](uml/After/Extract/ExtractField.svg?raw=true)

snippet: RefactoringSamples/Before/Extract/ExtractField.cs

becomes

snippet: RefactoringSamples/After/Extract/ExtractField.cs

#### Extract Field with Static members

![ExtractFieldStatic - Before](uml/Before/Extract/ExtractFieldStatic.svg?raw=true)

becomes

![ExtractFieldStatic - After](uml/After/Extract/ExtractFieldStatic.svg?raw=true)

snippet: RefactoringSamples/Before/Extract/ExtractFieldStatic.cs

becomes

snippet: RefactoringSamples/After/Extract/ExtractFieldStatic.cs

#### Extract Class

![ExtractClass - Before](uml/Before/Extract/ExtractClass.svg?raw=true)

becomes

![ExtractClass - After](uml/After/Extract/ExtractClass.svg?raw=true)

snippet: RefactoringSamples/Before/Extract/ExtractClass.cs

becomes

snippet: RefactoringSamples/After/Extract/ExtractClass.cs

#### Extract Superclass

![ExtractSuperclass - Before](uml/Before/Extract/ExtractSuperclass.svg?raw=true)

becomes

![ExtractSuperclass - After](uml/After/Extract/ExtractSuperclass.svg?raw=true)


snippet: RefactoringSamples/Before/Extract/ExtractSuperclass.cs

becomes

snippet: RefactoringSamples/After/Extract/ExtractSuperclass.cs

#### Extract Interface

![ExtractInterface - Before](uml/Before/Extract/ExtractInterface.svg?raw=true)

becomes

![ExtractInterface - After](uml/After/Extract/ExtractInterface.svg?raw=true)

snippet: RefactoringSamples/Before/Extract/ExtractInterface.cs

becomes

snippet: RefactoringSamples/After/Extract/ExtractInterface.cs

### Encapsulate Refactorings

#### Encapsulate Field

![EncapsulateField - Before](uml/Before/Encapsulate/EncapsulateField.svg?raw=true)

becomes

![EncapsulateField - After](uml/After/Encapsulate/EncapsulateField.svg?raw=true)


snippet: RefactoringSamples/Before/Encapsulate/EncapsulateField.cs

becomes

snippet: RefactoringSamples/After/Encapsulate/EncapsulateField.cs

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

* [JetBrains Rider Refactorings](https://www.jetbrains.com/help/rider/Refactorings__Index.html)

## Ideas

* Machine-generate markdown pages that show the Before and After of both the .cs source and the .svg files.
* Try generating combined .svg files that show the Before and After UML, with an arrow between the two.
