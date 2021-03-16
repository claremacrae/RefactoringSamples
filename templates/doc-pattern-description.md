# {{ data.source_file }}

toc

include: {{ data.source_file }}.description

## UML before and after

![{{ data.source_file }} - Before](../../uml/Before/{{ data.category }}/{{ data.source_file }}.svg?raw=true)

becomes

![{{ data.source_file }} - After](../../uml/After/{{ data.category }}/{{ data.source_file }}.svg?raw=true)

## Code before and after

snippet: {{ data.source_file }}-Before

becomes

snippet: {{ data.source_file }}-After

-----


