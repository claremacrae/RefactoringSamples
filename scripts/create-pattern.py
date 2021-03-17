#!/usr/bin/env python3
from typing import List

from scripts.constants import overwrite_if_exists
from scripts.file_from_template import FileFromTemplate
from scripts.inputs import Inputs
from scripts.outputs import Outputs
from scripts.refactoring import Refactoring
from scripts.refactoring_category import RefactoringCategory

Refactoring.templates = Refactoring.create_templates()


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
