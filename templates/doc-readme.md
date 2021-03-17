# Refactoring Samples

## Categories

{% for category in data.categories %}
* [{{ category.title }}]({{ category.category }}/){% for refactoring,title in category.refactorings_and_titles %}
  * [{{ title }}]({{ refactoring }}.md){% endfor %}{% endfor %}

## Reference

* "Refactoring: Improving the Design of Existing Code", Second Edition by Martin Fowler
    * [The Second Edition of "Refactoring"](https://martinfowler.com/articles/refactoring-2nd-ed.html)
    * [Accessing the web edition of Refactoring](https://martinfowler.com/articles/access-refactoring-web-edition.html)
    * [Online Catalog of Refactorings](https://refactoring.com/catalog/)
* [JetBrains Rider Refactorings](https://www.jetbrains.com/help/rider/Refactorings__Index.html)

