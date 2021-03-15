from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('../templates')
env = Environment(loader=file_loader)
template = env.get_template('refactoring-pattern.md')

refactoring = {}
refactoring['category'] = 'Extract'
refactoring['source_file'] = 'ExtractClass'

output = template.render(data=refactoring)
print(output)

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
