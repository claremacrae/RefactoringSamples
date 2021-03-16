#!/usr/bin/env python3
from typing import List

from jinja2 import Environment, FileSystemLoader

from scripts.constants import do_not_overwrite, overwrite_if_exists
from scripts.inputs import Inputs
from scripts.output_files import OutputFiles
from scripts.outputs import Outputs


def create_files(category, source_files):
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    files = get_per_refactoring_templates()

    refactoring = {}
    refactoring['category'] = category
    for source_file in source_files:
        refactoring['source_file'] = source_file
        for f in files.files:
            f.create_file(refactoring, env)


def get_per_refactoring_templates():
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


class RefactoringCategory:
    def __init__(self, category, refactorings):
        self.category = category
        self.refactorings = refactorings

    def create_files(self):
        create_files(self.category, self.refactorings)


class AllRefactorings:
    def __init__(self):
        self.categories: List[RefactoringCategory] = []

    def add_category(self, category: RefactoringCategory):
        self.categories.append(category)

    def create_files(self):
        for category in self.categories:
            category.create_files()


if __name__ == '__main__':
    all = AllRefactorings()
    all.add_category(RefactoringCategory('Encapsulate', [
        'EncapsulateField', ]))
    all.add_category(RefactoringCategory('Extract', [
        'ExtractClass',
        'ExtractField',
        'ExtractInterface',
        'ExtractSuperclass', ]))
    all.add_category(RefactoringCategory('IfStatements', [
        'RemoveRedundantElse', ]))

    all.create_files()

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
