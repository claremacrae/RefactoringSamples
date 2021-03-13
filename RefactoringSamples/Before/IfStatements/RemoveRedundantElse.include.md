
The IDE works out that the `else` statements are redundant,
because of the return statements.

Steps to improve the code:

Either

1. Click on first else, and select 'Remove redundant else'
2. Click on second else, and select 'Remove redundant else'
3. Click on third else, and select 'Remove redundant else'

Or

1. Click on first else, and select 'Remove redundant code in file'

![RemoveRedundantElse - Before](uml/Before/IfStatements/RemoveRedundantElse.svg?raw=true)

becomes

![RemoveRedundantElse - After](uml/After/IfStatements/RemoveRedundantElse.svg?raw=true)

snippet: RefactoringSamples/Before/IfStatements/RemoveRedundantElse.cs

becomes

snippet: RefactoringSamples/After/IfStatements/RemoveRedundantElse.cs
