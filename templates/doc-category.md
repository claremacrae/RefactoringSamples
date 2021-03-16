# {{ data.category }} Refactorings

Refactorings:
{% for refactoring in data.refactorings %}
* [{{ refactoring }}]({{ refactoring }}/){% endfor %}
