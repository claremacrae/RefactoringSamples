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
    #
    # RefactoringSamples/Before/Extract/ExtractClass.include.md
    extension = 'include.md'
    output_dir = F"../RefactoringSamples/Before/{refactoring['category']}/"
    output_file_name = output_dir + F"{refactoring['source_file']}.{extension}"
    with open(output_file_name, 'w') as f:
        output = template.render(data=refactoring)
        f.write(output)


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
