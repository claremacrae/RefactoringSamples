#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

from scripts.constants import do_not_overwrite, overwrite_if_exists
from scripts.inputs import Inputs
from scripts.output_files import OutputFiles
from scripts.outputs import Outputs


def create_files(category, source_files):
    refactoring = {}
    refactoring['category'] = category
    for source_file in source_files:
        refactoring['source_file'] = source_file
        create_files_impl(refactoring)


def create_files_impl(refactoring):
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    files = get_file_templates()
    for f in files.files:
        f.create_file(refactoring, env)


def get_file_templates():
    before = 'Before'
    after = 'After'
    files = OutputFiles()

    # Files in source tree
    outputs = Outputs('../RefactoringSamples/{{ stage }}/{{ data.category }}')
    for stage in [before, after]:
        files.add_file(Inputs('refactoring-pattern.cs', 'cs', stage, do_not_overwrite), outputs)

    files.add_file(Inputs('refactoring-pattern.md', 'include.md', before, overwrite_if_exists), outputs)

    files.add_file(Inputs('refactoring-pattern.description.md', 'description.include.md', before,
                                 do_not_overwrite), outputs)

    # Files in documentation tree
    outputs = Outputs('../docs/{{ data.category }}/mdsource')
    files.add_file(Inputs('doc-pattern-description.md', 'source.md', '', overwrite_if_exists), outputs)

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
