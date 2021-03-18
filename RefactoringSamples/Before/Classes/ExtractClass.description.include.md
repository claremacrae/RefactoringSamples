
## Summary

A class has grown too big, and you want to move some of its fields and/or methods to a new class

## Context

You have a class with some fields and/or methods that you wish to move to a different class.

Perhaps the class is doing too much, and you want to separate out some of its responsibilities.

## See Also

* [Extract Class refactoring](https://www.jetbrains.com/help/resharper/Refactorings__Extract_Class.html) (JetBrains ReSharper)
    * Note that this [is implemented in Rider](https://youtrack.jetbrains.com/issue/RIDER-7903) but is not in the documentation, as of March 2021
* [Extract Class](https://refactoring.com/catalog/extractClass.html) (Refactoring.com)

## Steps to improve the code

* Select the class name, and say "Refactor This" -> "Extract Class"
* Select any fields and/or methods that you want to move
* Enter a name for the extracted class

Notes:

* Any fields in the original class will be replaced by an instance of the new class, and the code updated accordingly.
