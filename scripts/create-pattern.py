from jinja2 import Environment, FileSystemLoader


def create_files():
    refactoring = {}
    refactoring['category'] = 'Extract'
    refactoring['source_file'] = 'ExtractClass'

    create_files_impl(refactoring)


def create_files_impl(refactoring):
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    template = env.get_template('refactoring-pattern.md')
    output = template.render(data=refactoring)
    print(output)


if __name__ == '__main__':
    create_files()

"""
{% if truth %}
{% else %}
{% endif %}

colors = ['red', 'green', 'blue']
{% for color in colors %}
    {{ color }}
{% endfor %}

{% include 'header.html %}

See also extending templates, and embedding blocks

"""
