from typing import List

from scripts.constants import overwrite_if_exists
from scripts.file_from_template import FileFromTemplate
from scripts.inputs import Inputs
from scripts.outputs import Outputs
from scripts.refactoring_category import RefactoringCategory


class AllRefactorings:
    def __init__(self) -> None:
        self.categories: List[RefactoringCategory] = []

    def add_category(self, category: RefactoringCategory) -> None:
        self.categories.append(category)

    def create_files(self) -> None:
        self.create_doc_readme()
        self.create_per_category_files()

    def create_per_category_files(self) -> None:
        for category in self.categories:
            category.create_files()

    def create_doc_readme(self) -> None:
        inputs = Inputs('doc-readme.md', 'source.md', '', overwrite_if_exists)
        outputs = Outputs('../docs/mdsource')
        template = FileFromTemplate(inputs, outputs)

        template.create_file(self.as_dictionary())

    def as_dictionary(self):
        return {
            'source_file': 'README',
            'categories': [category.as_dictionary() for category in self.categories]
        }
