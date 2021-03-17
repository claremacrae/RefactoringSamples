#!/usr/bin/env python3
from typing import List

from scripts.constants import overwrite_if_exists
from scripts.file_from_template import FileFromTemplate
from scripts.helpers import remove_spaces
from scripts.inputs import Inputs
from scripts.outputs import Outputs
from scripts.refactoring import Refactoring

Refactoring.templates = Refactoring.create_templates()


class RefactoringCategory:
    def __init__(self, title, refactorings):
        self.category = remove_spaces(title)
        self.title = title
        self.titles = refactorings
        self.refactorings = [remove_spaces(x) for x in refactorings]

    def create_files(self):
        self.create_category_readme()
        for title in self.titles:
            r = Refactoring(title)
            r.create_files(self.title)

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
        'Extract Interface',
        'Extract Superclass', ]))
    all.add_category(RefactoringCategory('If Statements', [
        'Remove Redundant Else', ]))
    all.add_category(RefactoringCategory('Introduce', [
        'Introduce Field', ]))

    all.create_files()
