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

<!-- snippet: ExtractField-Before -->
<a id='snippet-extractfield-before'></a>
```cs
public class ExtractField
{
    public void LongMethod()
    {
        int thing1;
        int thing2;
        int thing3;
    }
}
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractField.cs#L3-L13' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractfield-before' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: ExtractField-After -->
<a id='snippet-extractfield-after'></a>
```cs
public class ExtractField
{
    private int _thing1;
    private int _thing2;
    private int _thing3;

    public void LongMethod()
    {
    }
}
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractField.cs#L3-L14' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractfield-after' title='Start of snippet'>anchor</a></sup>
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

<!-- snippet: ExtractFieldStatic-Before -->
<a id='snippet-extractfieldstatic-before'></a>
```cs
public class ExtractFieldStatic
{
    public static void LongMethod()
    {
        int thing1;
        int thing2;
        int thing3;
    }
}
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractFieldStatic.cs#L3-L13' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractfieldstatic-before' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: ExtractFieldStatic-After -->
<a id='snippet-extractfieldstatic-after'></a>
```cs
public class ExtractFieldStatic
{
    private static int _thing1;
    private static int _thing2;
    private static int _thing3;

    public static void LongMethod()
    {
    }
}
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractFieldStatic.cs#L3-L14' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractfieldstatic-after' title='Start of snippet'>anchor</a></sup>
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

<!-- snippet: ExtractClass-Before -->
<a id='snippet-extractclass-before'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractClass.cs#L3-L19' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractclass-before' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: ExtractClass-After -->
<a id='snippet-extractclass-after'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractClass.cs#L3-L29' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractclass-after' title='Start of snippet'>anchor</a></sup>
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

<!-- snippet: ExtractSuperclass-Before -->
<a id='snippet-extractsuperclass-before'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractSuperclass.cs#L3-L16' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractsuperclass-before' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: ExtractSuperclass-After -->
<a id='snippet-extractsuperclass-after'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractSuperclass.cs#L3-L20' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractsuperclass-after' title='Start of snippet'>anchor</a></sup>
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

<!-- snippet: ExtractInterface-Before -->
<a id='snippet-extractinterface-before'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/Before/Extract/ExtractInterface.cs#L3-L16' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractinterface-before' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: ExtractInterface-After -->
<a id='snippet-extractinterface-after'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/After/Extract/ExtractInterface.cs#L3-L22' title='Snippet source file'>snippet source</a> | <a href='#snippet-extractinterface-after' title='Start of snippet'>anchor</a></sup>
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

<!-- snippet: EncapsulateField-Before -->
<a id='snippet-encapsulatefield-before'></a>
```cs
public class EncapsulateField
{
    private int _thing1;
    private int _thing2;
}
```
<sup><a href='/RefactoringSamples/Before/Encapsulate/EncapsulateField.cs#L3-L9' title='Snippet source file'>snippet source</a> | <a href='#snippet-encapsulatefield-before' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: EncapsulateField-After -->
<a id='snippet-encapsulatefield-after'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/After/Encapsulate/EncapsulateField.cs#L3-L16' title='Snippet source file'>snippet source</a> | <a href='#snippet-encapsulatefield-after' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

-----
 <!-- endInclude -->

### If Statements

<!-- #### Invert If -->

#### Remove Redundant Else

 <!-- include: RemoveRedundantElse. path: /RefactoringSamples/Before/IfStatements/RemoveRedundantElse.include.md -->
##### Context

##### Steps to improve the code

##### UML before and after

![RemoveRedundantElse - Before](uml/Before/IfStatements/RemoveRedundantElse.svg?raw=true)

becomes

![RemoveRedundantElse - After](uml/After/IfStatements/RemoveRedundantElse.svg?raw=true)

##### Code before and after

<!-- snippet: RemoveRedundantElse-Before -->
<a id='snippet-removeredundantelse-before'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/Before/IfStatements/RemoveRedundantElse.cs#L7-L31' title='Snippet source file'>snippet source</a> | <a href='#snippet-removeredundantelse-before' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

becomes

<!-- snippet: RemoveRedundantElse-After -->
<a id='snippet-removeredundantelse-after'></a>
```cs
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
```
<sup><a href='/RefactoringSamples/After/IfStatements/RemoveRedundantElse.cs#L7-L27' title='Snippet source file'>snippet source</a> | <a href='#snippet-removeredundantelse-after' title='Start of snippet'>anchor</a></sup>
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
