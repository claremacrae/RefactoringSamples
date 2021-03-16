<!--
GENERATED FILE - DO NOT EDIT
This file was generated by [MarkdownSnippets](https://github.com/SimonCropp/MarkdownSnippets).
Source File: /docs/Extract/mdsource/ExtractClass.source.md
To change this file edit the source file and then execute ./run_markdown_templates.sh.
-->

# ExtractClass

<!-- toc -->
## Contents

  * [UML before and after](#uml-before-and-after)
  * [Code before and after](#code-before-and-after)<!-- endToc -->

 <!-- include: ExtractClass.description. path: /RefactoringSamples/Before/Extract/ExtractClass.description.include.md -->
#### Context

#### See Also

#### Steps to improve the code <!-- endInclude -->

## UML before and after

![ExtractClass - Before](../../uml/Before/Extract/ExtractClass.svg?raw=true)

becomes

![ExtractClass - After](../../uml/After/Extract/ExtractClass.svg?raw=true)

## Code before and after

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
