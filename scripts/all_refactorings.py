from typing import List

from scripts.constants import overwrite_if_exists
from scripts.file_from_template import FileFromTemplate
from scripts.inputs import Inputs
from scripts.outputs import Outputs
from scripts.refactoring_category import RefactoringCategory


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
        categories = []
        for category in self.categories:
            categories.append(category.as_dictionary())
        refactoring['categories'] = categories
        return refactoring