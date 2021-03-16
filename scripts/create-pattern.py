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

    def create_file(self, refactoring, env):
        template = env.get_template(self.template_name)
        output_file_name = F"../RefactoringSamples/{self.stage}/{refactoring['category']}/{refactoring['source_file']}.{self.extension}"
        if os.path.exists(output_file_name) and self.overwrite_if_existing == do_not_overwrite:
            print(f'File already exists: not overwriting: {output_file_name}')
            return
        with open(output_file_name, 'w') as f:
            output = template.render(data=refactoring, stage=self.stage)
            f.write(output)


def create_files_impl(refactoring):
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    files = get_file_templates()
    for f in files:
        f.create_file(refactoring, env)


def get_file_templates():
    before = 'Before'
    after = 'After'
    files = []
    for stage in [before, after]:
        files.append(FileFromTemplate('refactoring-pattern.cs', 'cs', stage, do_not_overwrite))
    files.append(FileFromTemplate('refactoring-pattern.md', 'include.md', before, overwrite_if_exists))
    files.append(
        FileFromTemplate('refactoring-pattern.description.md', 'description.include.md', before, do_not_overwrite))
    return files


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
