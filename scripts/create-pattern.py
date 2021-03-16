#!/usr/bin/env python3

import os

from jinja2 import Environment, FileSystemLoader


def create_files(category, source_files):
    refactoring = {}
    refactoring['category'] = category
    for source_file in source_files:
        refactoring['source_file'] = source_file
        create_files_impl(refactoring)

do_not_overwrite = False
overwrite_if_exists = True


class FileFromTemplate(object):
    def __init__(self, template_name, extension, stage, overwrite_if_existing):
        self.template_name = template_name
        self.extension = extension
        self.stage = stage
        self.overwrite_if_existing = overwrite_if_existing


def create_files_impl(refactoring):
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    before = 'Before'
    after = 'After'
    for stage in [before, after]:
        create_file_from_template(refactoring, env, 'refactoring-pattern.cs', 'cs', stage, do_not_overwrite)
    create_file_from_template(refactoring, env, 'refactoring-pattern.md', 'include.md', before, overwrite_if_exists)
    create_file_from_template(refactoring, env, 'refactoring-pattern.description.md', 'description.include.md', before,
                              do_not_overwrite)


def create_file_from_template(refactoring, env, template_name, extension, stage, overwrite_if_existing):
    template = env.get_template(template_name)
    output_file_name = F"../RefactoringSamples/{stage}/{refactoring['category']}/{refactoring['source_file']}.{extension}"
    if os.path.exists(output_file_name) and overwrite_if_existing == do_not_overwrite:
        print(f'File already exists: not overwriting: {output_file_name}')
        return
    with open(output_file_name, 'w') as f:
        output = template.render(data=refactoring, stage=stage)
        f.write(output)


if __name__ == '__main__':
    create_files('Encapsulate', [
        'EncapsulateField', ])
    create_files('Extract', [
        'ExtractClass',
        'ExtractField',
        'ExtractInterface',
        'ExtractSuperclass', ])
    create_files('IfStatements', [
        'RemoveRedundantElse', ])

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
