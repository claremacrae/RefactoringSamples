# {{ data.title }}

[Top](../) / [{{ data.category_title }}](.) / **{{ data.title }}**

toc

include: {{ data.source_file }}.description

## UML before and after

**Before refactoring**

![{{ data.source_file }} - Before](../../uml/Before/{{ data.category }}/{{ data.source_file }}.svg?raw=true)

**After refactoring**

![{{ data.source_file }} - After](../../uml/After/{{ data.category }}/{{ data.source_file }}.svg?raw=true)

## Code before and after

**Before refactoring**

snippet: {{ data.source_file }}-Before

**After refactoring**

snippet: {{ data.source_file }}-After

-----


