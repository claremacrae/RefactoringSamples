<!--
GENERATED FILE - DO NOT EDIT
This file was generated by [MarkdownSnippets](https://github.com/SimonCropp/MarkdownSnippets).
Source File: /mdsource/README.source.md
To change this file edit the source file and then execute ./run_markdown_templates.sh.
-->

<a id="top"></a>

# RefactoringSamples

<!-- toc -->
## Contents

  * [Purpose](#purpose)
  * [Refactoring Samples](#refactoring-samples)
    * [Key](#key)
    * [Extract Refactorings](#extract-refactorings)
      * [Extract Field](#extract-field)
      * [Extract Field with Static members](#extract-field-with-static-members)
      * [Extract Class](#extract-class)
      * [Extract Superclass](#extract-superclass)
      * [Extract Interface](#extract-interface)
    * [Encapsulate Refactorings](#encapsulate-refactorings)
      * [Encapsulate Field](#encapsulate-field)
    * [If Statements](#if-statements)
      * [Remove Redundant Else](#remove-redundant-else)
  * [Creating a new pair of files](#creating-a-new-pair-of-files)
  * [Reference](#reference)
  * [Ideas](#ideas)<!-- endToc -->

## Purpose

To provide visualisations of micro-refactorings in C# code, using UML diagrams generated from pairs of tiny C# source files.

## Refactoring Samples

### Key

![Key](uml/Keys/Key.svg?raw=true)

### Extract Refactorings

<!-- #### Extract Method -->

<!-- #### Extract Variable -->

#### Extract Field

 <!-- include: ExtractField. path: /RefactoringSamples/Before/Extract/ExtractField.include.md -->
##### Context

##### Steps to improve the code

##### UML before and after

![ExtractField - Before](uml/Before/Extract/ExtractField.svg?raw=true)

becomes

![ExtractField - After](uml/After/Extract/ExtractField.svg?raw=true)

##### Code before and after

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

-----
 <!-- endInclude -->

#### Extract Field with Static members

 <!-- include: ExtractFieldStatic. path: /RefactoringSamples/Before/Extract/ExtractFieldStatic.include.md -->
##### Context

##### Steps to improve the code

##### UML before and after

![ExtractFieldStatic - Before](uml/Before/Extract/ExtractFieldStatic.svg?raw=true)

becomes

![ExtractFieldStatic - After](uml/After/Extract/ExtractFieldStatic.svg?raw=true)

##### Code before and after

<!-- snippet: RefactoringSamples/Before/Extract/ExtractFieldStatic.cs -->
<a id='snippet-RefactoringSamples/Before/Extract/ExtractFieldStatic.cs'></a>
```cs
namespace RefactoringSamples.Before.Extract
{
    public class ExtractFieldStatic
    {
        public static void LongMethod()
        {
            int thing1;
            int thing2;
            int thing3;
        }
    }
}
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractFieldStatic.cs#L1-L12' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/Before/Extract/ExtractFieldStatic.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RefactoringSamples/After/Extract/ExtractFieldStatic.cs -->
<a id='snippet-RefactoringSamples/After/Extract/ExtractFieldStatic.cs'></a>
```cs
namespace RefactoringSamples.After.Extract
{
    public class ExtractFieldStatic
    {
        private static int _thing1;
        private static int _thing2;
        private static int _thing3;

        public static void LongMethod()
        {
        }
    }
}
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractFieldStatic.cs#L1-L13' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/After/Extract/ExtractFieldStatic.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

-----
 <!-- endInclude -->

#### Extract Class

 <!-- include: ExtractClass. path: /RefactoringSamples/Before/Extract/ExtractClass.include.md -->
##### Context

##### Steps to improve the code

##### UML before and after

![ExtractClass - Before](uml/Before/Extract/ExtractClass.svg?raw=true)

becomes

![ExtractClass - After](uml/After/Extract/ExtractClass.svg?raw=true)

##### Code before and after

<!-- snippet: RefactoringSamples/Before/Extract/ExtractClass.cs -->
<a id='snippet-RefactoringSamples/Before/Extract/ExtractClass.cs'></a>
```cs
namespace RefactoringSamples.Before.Extract
{
    public class ExtractClass
    {
        private int _concept1;
        private int _concept2;

        public int Concept1Function()
        {
            return _concept1;
        }

        public int Concept2Function()
        {
            return _concept2;
        }
    }
}
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractClass.cs#L1-L18' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/Before/Extract/ExtractClass.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RefactoringSamples/After/Extract/ExtractClass.cs -->
<a id='snippet-RefactoringSamples/After/Extract/ExtractClass.cs'></a>
```cs
namespace RefactoringSamples.After.Extract
{
    public class Concept1
    {
        private int _concept1;

        public int Concept1Function()
        {
            return _concept1;
        }
    }

    public class Concept2
    {
        private int _concept2;

        public int Concept2Function()
        {
            return _concept2;
        }
    }

    public class ExtractClass
    {
        private readonly Concept1 _concept1 = new Concept1();
        private readonly Concept2 _concept2 = new Concept2();
    }
}
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractClass.cs#L1-L28' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/After/Extract/ExtractClass.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

-----
 <!-- endInclude -->

#### Extract Superclass

 <!-- include: ExtractSuperclass. path: /RefactoringSamples/Before/Extract/ExtractSuperclass.include.md -->
##### Context

##### Steps to improve the code

##### UML before and after

![ExtractSuperclass - Before](uml/Before/Extract/ExtractSuperclass.svg?raw=true)

becomes

![ExtractSuperclass - After](uml/After/Extract/ExtractSuperclass.svg?raw=true)

##### Code before and after

<!-- snippet: RefactoringSamples/Before/Extract/ExtractSuperclass.cs -->
<a id='snippet-RefactoringSamples/Before/Extract/ExtractSuperclass.cs'></a>
```cs
namespace RefactoringSamples.Before.Extract
{
    public class ExtractSuperclass
    {
        public int method1()
        {
            return 0;
        }

        public int method2()
        {
            return 0;
        }
    }
}
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractSuperclass.cs#L1-L15' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/Before/Extract/ExtractSuperclass.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RefactoringSamples/After/Extract/ExtractSuperclass.cs -->
<a id='snippet-RefactoringSamples/After/Extract/ExtractSuperclass.cs'></a>
```cs
namespace RefactoringSamples.After.Extract
{
    public class ExtractSuperclassBase
    {
        public int method1()
        {
            return 0;
        }

        public int method2()
        {
            return 0;
        }
    }

    public class ExtractSuperclass : ExtractSuperclassBase
    {
    }
}
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractSuperclass.cs#L1-L19' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/After/Extract/ExtractSuperclass.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

-----
 <!-- endInclude -->

#### Extract Interface

 <!-- include: ExtractInterface. path: /RefactoringSamples/Before/Extract/ExtractInterface.include.md -->
##### Context

##### Steps to improve the code

##### UML before and after

![ExtractInterface - Before](uml/Before/Extract/ExtractInterface.svg?raw=true)

becomes

![ExtractInterface - After](uml/After/Extract/ExtractInterface.svg?raw=true)

##### Code before and after

<!-- snippet: RefactoringSamples/Before/Extract/ExtractInterface.cs -->
<a id='snippet-RefactoringSamples/Before/Extract/ExtractInterface.cs'></a>
```cs
namespace RefactoringSamples.Before.Extract
{
    public class ExtractInterface
    {
        public int method1()
        {
            return 0;
        }

        public int method2()
        {
            return 0;
        }
    }
}
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractInterface.cs#L1-L15' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/Before/Extract/ExtractInterface.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RefactoringSamples/After/Extract/ExtractInterface.cs -->
<a id='snippet-RefactoringSamples/After/Extract/ExtractInterface.cs'></a>
```cs
namespace RefactoringSamples.After.Extract
{
    public interface IExtractInterface
    {
        public int method1();
        public int method2();
    }

    public class ExtractInterface : IExtractInterface
    {
        public int method1()
        {
            return 0;
        }

        public int method2()
        {
            return 0;
        }
    }
}
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractInterface.cs#L1-L21' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/After/Extract/ExtractInterface.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

-----
 <!-- endInclude -->

### Encapsulate Refactorings

#### Encapsulate Field

 <!-- include: EncapsulateField. path: /RefactoringSamples/Before/Encapsulate/EncapsulateField.include.md -->
##### Context

##### Steps to improve the code

##### UML before and after

![EncapsulateField - Before](uml/Before/Encapsulate/EncapsulateField.svg?raw=true)

becomes

![EncapsulateField - After](uml/After/Encapsulate/EncapsulateField.svg?raw=true)

##### Code before and after

<!-- snippet: RefactoringSamples/Before/Encapsulate/EncapsulateField.cs -->
<a id='snippet-RefactoringSamples/Before/Encapsulate/EncapsulateField.cs'></a>
```cs
namespace RefactoringSamples.Before.Encapsulate
{
    public class EncapsulateField
    {
        private int _thing1;
        private int _thing2;
    }
}
```
<sup><a href='/RefactoringSamples/Before/Encapsulate/EncapsulateField.cs#L1-L8' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/Before/Encapsulate/EncapsulateField.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RefactoringSamples/After/Encapsulate/EncapsulateField.cs -->
<a id='snippet-RefactoringSamples/After/Encapsulate/EncapsulateField.cs'></a>
```cs
namespace RefactoringSamples.After.Encapsulate
{
    public class EncapsulateField
    {
        public int Thing1AsAutoProperty { get; }

        public int Thing2
        {
            get => _thing2;
            set => _thing2 = value;
        }

        private int _thing2;
    }
}
```
<sup><a href='/RefactoringSamples/After/Encapsulate/EncapsulateField.cs#L1-L15' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/After/Encapsulate/EncapsulateField.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

-----
 <!-- endInclude -->

### If Statements

<!-- #### Invert If -->

#### Remove Redundant Else

 <!-- include: RemoveRedundantElse. path: /RefactoringSamples/Before/IfStatements/RemoveRedundantElse.include.md -->
##### Context

The IDE works out that the `else` statements are redundant,
because of the return statements.

##### Steps to improve the code

Either

1. Click on first else, and select 'Remove redundant else'
2. Click on second else, and select 'Remove redundant else'
3. Click on third else, and select 'Remove redundant else'

Or

1. Click on first else, and select 'Remove redundant code in file'

##### UML before and after

![RemoveRedundantElse - Before](uml/Before/IfStatements/RemoveRedundantElse.svg?raw=true)

becomes

![RemoveRedundantElse - After](uml/After/IfStatements/RemoveRedundantElse.svg?raw=true)

##### Code before and after

<!-- snippet: RefactoringSamples/Before/IfStatements/RemoveRedundantElse.cs -->
<a id='snippet-RefactoringSamples/Before/IfStatements/RemoveRedundantElse.cs'></a>
```cs
using System;

namespace RefactoringSamples.Before.IfStatements
{
    public class RemoveRedundantElse
    {
        public string HeavilyNestedIf()
        {
            if ((new Random().Next() % 3) == 0)
            {
                return "Multiple of 3";
            }
            else
            {
                if ((new Random().Next() % 4) == 0)
                {
                    return "Multiple of 4";
                }
                else
                {
                    if ((new Random().Next() % 5) == 0)
                    {
                        return "Multiple of 5";
                    }
                }
            }

            return "Value not recognised";
        }
    }
}
```
<sup><a href='/RefactoringSamples/Before/IfStatements/RemoveRedundantElse.cs#L1-L31' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/Before/IfStatements/RemoveRedundantElse.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RefactoringSamples/After/IfStatements/RemoveRedundantElse.cs -->
<a id='snippet-RefactoringSamples/After/IfStatements/RemoveRedundantElse.cs'></a>
```cs
using System;

namespace RefactoringSamples.After.IfStatements
{
    public class RemoveRedundantElse
    {
        public string HeavilyNestedIf()
        {
            if ((new Random().Next() % 3) == 0)
            {
                return "Multiple of 3";
            }

            if ((new Random().Next() % 4) == 0)
            {
                return "Multiple of 4";
            }

            if ((new Random().Next() % 5) == 0)
            {
                return "Multiple of 5";
            }

            return "Value not recognised";
        }
    }
}
```
<sup><a href='/RefactoringSamples/After/IfStatements/RemoveRedundantElse.cs#L1-L27' title='Snippet source file'>snippet source</a> | <a href='#snippet-RefactoringSamples/After/IfStatements/RemoveRedundantElse.cs' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

-----
 <!-- endInclude -->

## Creating a new pair of files

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
