#!/usr/bin/env python3
from typing import List

from scripts.constants import do_not_overwrite, overwrite_if_exists
from scripts.file_from_template import FileFromTemplate
from scripts.inputs import Inputs
from scripts.output_files import OutputFiles
from scripts.outputs import Outputs


def create_files(category, source_files):
    files = get_per_refactoring_templates()

    refactoring = {}
    refactoring['category'] = category
    for source_file in source_files:
        refactoring['source_file'] = source_file
        for f in files.files:
            f.create_file(refactoring)


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
    def __init__(self, title, refactorings):
        self.category = title.replace(' ', '')
        self.title = title
        self.titles = refactorings
        self.refactorings = [x.replace(' ', '') for x in refactorings]

    def create_files(self):
        self.create_category_readme()
        create_files(self.category, self.refactorings)

    def create_category_readme(self):
        inputs = Inputs('doc-category.md', 'source.md', '', overwrite_if_exists)
        outputs = Outputs('../docs/{{ data.category }}/mdsource')
        template = FileFromTemplate(inputs, outputs)

        refactoring = self.as_dictionary()
        template.create_file(refactoring)

    def as_dictionary(self):
        refactoring = dict()
        refactoring['source_file'] = 'README'
        refactoring['category'] = self.category
        refactoring['title'] = self.title
        refactoring['refactorings'] = [x for x in self.refactorings]
        refactoring['refactorings_and_titles'] = zip(self.refactorings, self.titles)
        return refactoring


class AllRefactorings:
    def __init__(self):
        self.categories: List[RefactoringCategory] = []

    def add_category(self, category: RefactoringCategory):
        self.categories.append(category)

    def create_files(self):
        self.create_doc_readme()
        self.create_per_category_files()

    def create_per_category_files(self):
        for category in self.categories:
            category.create_files()

    def create_doc_readme(self):
        inputs = Inputs('doc-readme.md', 'source.md', '', overwrite_if_exists)
        outputs = Outputs('../docs/mdsource')
        template = FileFromTemplate(inputs, outputs)

        template.create_file(self.as_dictionary())

    def as_dictionary(self):
        refactoring = dict()
        refactoring['source_file'] = 'README'
        refactoring['categories_and_titles'] = zip([x.category for x in self.categories],
                                                   [x.title for x in self.categories])
        return refactoring


if __name__ == '__main__':
    all = AllRefactorings()
    all.add_category(RefactoringCategory('Encapsulate', [
        'Encapsulate Field', ]))
    all.add_category(RefactoringCategory('Extract', [
        'Extract Class',
        'Extract Field',
        'Extract Interface',
        'Extract Superclass', ]))
    all.add_category(RefactoringCategory('If Statements', [
        'Remove Redundant Else', ]))

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
