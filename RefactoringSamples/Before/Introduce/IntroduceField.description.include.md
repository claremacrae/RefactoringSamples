
## Context

You have a variable or expression in a method, and you want to make it a field.

If you select a variable, at the point it is declared, then it gets moved to be a field.

If you select an expression, then no existing variables are removed. If the expression occurs more than once, you will have the option to replace all of the occurrences.

Also known as "Introduce Field".

Applications:

* There is a repeated expression in the code, such as repeated magic numbers, and you want to replace all repeated magic numbers and expressions with single value, such as a constant.
* You want to start dividing a long method up, and make it a class. Some locals inside the method may become fields in the new class. Or you may want to avoid needing to pass them around as parameters to methods you will be extracting.

Having introduced one or more fields, you can then "Extract Class" to group them together, in a separate class.

## See Also

* [Introduce Field refactoring](https://www.jetbrains.com/help/rider/Refactorings__Introduce_Field.html) (JetBrains Rider)

## Steps to improve the code

* Select the expression, and say "Refactor This" -> "Introduce Field"
* If there are multiple occurrences of the expression, say if you want to replace one or all.
* Give the new field a name.

Notes:

* if the field was extracted from a non-static method, the new field will be non-static.
* if the field was extracted from a static method, the new field will be static.
