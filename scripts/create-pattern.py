from jinja2 import Environment, FileSystemLoader


def create_files(category, source_file):
    refactoring = {}
    refactoring['category'] = category
    refactoring['source_file'] = source_file

    create_files_impl(refactoring)


def create_files_impl(refactoring):
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    before = 'Before'
    after = 'After'
    for stage in [before, after]:
        create_file_from_template(refactoring, stage, env, 'refactoring-pattern.cs', 'cs')
    create_file_from_template(refactoring, before, env, 'refactoring-pattern.md', 'include.md')


def create_file_from_template(refactoring, stage, env, template_name, extension):
    template = env.get_template(template_name)
    output_file_name = F"../RefactoringSamples/{stage}/{refactoring['category']}/{refactoring['source_file']}.{extension}"
    with open(output_file_name, 'w') as f:
        output = template.render(data=refactoring, stage=stage)
        f.write(output)


if __name__ == '__main__':
    create_files('Extract', 'TestClass')

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
