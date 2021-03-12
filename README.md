# RefactoringSamples

<!-- toc -->
## Contents

  * [Purpose](#purpose)
  * [Refactoring Demos](#refactoring-demos)
    * [Extract Refactorings](#extract-refactorings)
      * [Extract Field](#extract-field)
      * [Extract Field with Static members](#extract-field-with-static-members)
      * [Extract Class](#extract-class)
      * [Extract Superclass](#extract-superclass)
      * [Extract Interface](#extract-interface)
    * [Encapsulate Refactorings](#encapsulate-refactorings)
      * [Encapsulate Field](#encapsulate-field)
  * [Creating a new pair of files](#creating-a-new-pair-of-files)
  * [Reference](#reference)
  * [Ideas](#ideas)<!-- endToc -->

## Purpose

To provide visualisations of micro-refactorings in C# code

## Refactoring Demos

### Extract Refactorings

#### Extract Field

![ExtractField - Before](uml/Before/Extract/ExtractField.svg?raw=true)

becomes

![ExtractField - After](uml/After/Extract/ExtractField.svg?raw=true)

<!-- snippet: RefactoringSamples/Before/Extract/ExtractField.cs -->
<a id='snippet-RefactoringSamples/Before/Extract/ExtractField.cs'></a>
```cs
namespace RefactoringSamples.Before.Extract
{
    public class ExtractField
    {
        public void LongMethod()
        {
            int thing1;
            int thing2;
            int thing3;
        }
    }
}
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractField.cs#L1-L12' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/Before/Extract/ExtractField.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RefactoringSamples/After/Extract/ExtractField.cs -->
<a id='snippet-RefactoringSamples/After/Extract/ExtractField.cs'></a>
```cs
namespace RefactoringSamples.After.Extract
{
    public class ExtractField
    {
        private int _thing1;
        private int _thing2;
        private int _thing3;

        public void LongMethod()
        {
        }
    }
}
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractField.cs#L1-L13' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/After/Extract/ExtractField.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

#### Extract Field with Static members

![ExtractFieldStatic - Before](uml/Before/Extract/ExtractFieldStatic.svg?raw=true)

becomes

![ExtractFieldStatic - After](uml/After/Extract/ExtractFieldStatic.svg?raw=true)

#### Extract Class

![ExtractClass - Before](uml/Before/Extract/ExtractClass.svg?raw=true)

becomes

![ExtractClass - After](uml/After/Extract/ExtractClass.svg?raw=true)

#### Extract Superclass

![ExtractSuperclass - Before](uml/Before/Extract/ExtractSuperclass.svg?raw=true)

becomes

![ExtractSuperclass - After](uml/After/Extract/ExtractSuperclass.svg?raw=true)


#### Extract Interface

![ExtractInterface - Before](uml/Before/Extract/ExtractInterface.svg?raw=true)

becomes

![ExtractInterface - After](uml/After/Extract/ExtractInterface.svg?raw=true)

### Encapsulate Refactorings

#### Encapsulate Field

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
