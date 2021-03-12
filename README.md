# RefactoringSamples

## Purpose

To provide visualisations of micro-refactorings in C# code

## Extract Refactorings

### Extract Field

![ExtractField - Before](uml/Before/Extract/ExtractField.svg?raw=true)

becomes

![ExtractField - After](uml/After/Extract/ExtractField.svg?raw=true)

### Extract Field with Static members

![ExtractFieldStatic - Before](uml/Before/Extract/ExtractFieldStatic.svg?raw=true)

becomes

![ExtractFieldStatic - After](uml/After/Extract/ExtractFieldStatic.svg?raw=true)

![ExtractClass - Before](uml/Before/Extract/ExtractClass.svg?raw=true)

becomes

![ExtractClass - After](uml/After/Extract/ExtractClass.svg?raw=true)

### Extract Superclass

![ExtractSuperclass - Before](uml/Before/Extract/ExtractSuperclass.svg?raw=true)

becomes

![ExtractSuperclass - After](uml/After/Extract/ExtractSuperclass.svg?raw=true)


### Extract Interface

![ExtractInterface - Before](uml/Before/Extract/ExtractInterface.svg?raw=true)

becomes

![ExtractInterface - After](uml/After/Extract/ExtractInterface.svg?raw=true)

## Encapsulate Refactorings

### Extract Interface

![EncapsulateField - Before](uml/Before/Encapsulate/EncapsulateField.svg?raw=true)

becomes

![EncapsulateField - After](uml/After/Encapsulate/EncapsulateField.svg?raw=true)


## Creating a new pair of files

1. Create a new .cs file in a sub-dir of `RefactoringSamples/Before`
1. Set it up with the methods and fields that you want to demo
1. Make sure its namespace matches its location
1. Select the class name and Refactor This and Copy Type
    * Change the namespace from Before to After
1. In the new file, apply the refactoring
1. Run `create-uml.bat`
1. Review and commit the files

## Reference

* [JetBrains Rider Refactorings](https://www.jetbrains.com/help/rider/Refactorings__Index.html)

## Ideas

* Machine-generate markdown pages that show the Before and After of both the .cs source and the .svg files.
* Try generating combined .svg files that show the Before and After UML, with an arrow between the two.
