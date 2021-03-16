# {{ data.title }} Refactorings

[Top](../) / **{{ data.title }}**

Refactorings:
{% for refactoring,title in data.refactorings_and_titles %}
* [{{ title }}]({{ refactoring }}.md){% endfor %}
