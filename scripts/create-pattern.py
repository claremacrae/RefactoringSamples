#!/usr/bin/env python3
from typing import List

from scripts.constants import do_not_overwrite, overwrite_if_exists
from scripts.file_from_template import FileFromTemplate
from scripts.inputs import Inputs
from scripts.output_files import OutputFiles
from scripts.outputs import Outputs


def remove_spaces(text):
    return text.replace(' ', '')


def create_files(category_title, titles):
    files = get_per_refactoring_templates()

    for title in titles:
        r = Refactoring(title)
        r.create_files(category_title)


def get_per_refactoring_templates():
    before = 'Before'
    after = 'After'
    files = OutputFiles()

    # Files in source tree
    outputs = Outputs('../RefactoringSamples/{{ stage }}/{{ data.category }}')
    for stage in [before, after]:
        files.add_file(Inputs('refactoring-pattern.cs', 'cs', stage, do_not_overwrite), outputs)

    files.add_file(Inputs('refactoring-pattern.description.md', 'description.include.md', before,
                                 do_not_overwrite), outputs)

    # Files in documentation tree
    outputs = Outputs('../docs/{{ data.category }}/mdsource')
    files.add_file(Inputs('doc-pattern-description.md', 'source.md', '', overwrite_if_exists), outputs)

    return files


# TODO Move code above in to this class, and start using it
class Refactoring:
    templates = None

    def __init__(self, title):
        self.title = title

    def create_files(self, category_title):
        refactoring = self.as_dictionary(category_title)
        for f in Refactoring.templates.files:
            f.create_file(refactoring)

    def as_dictionary(self, category_title):
        refactoring = {}
        refactoring['category'] = remove_spaces(category_title)
        refactoring['category_title'] = category_title
        refactoring['source_file'] = remove_spaces(self.title)
        refactoring['title'] = self.title
        return refactoring

    @staticmethod
    def create_templates():
        return get_per_refactoring_templates()


Refactoring.templates = Refactoring.create_templates()


class RefactoringCategory:
    def __init__(self, title, refactorings):
        self.category = remove_spaces(title)
        self.title = title
        self.titles = refactorings
        self.refactorings = [remove_spaces(x) for x in refactorings]

    def create_files(self):
        self.create_category_readme()
        create_files(self.title, self.titles)

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
