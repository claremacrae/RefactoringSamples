from scripts.constants import overwrite_if_exists
from scripts.file_from_template import FileFromTemplate
from scripts.helpers import remove_spaces
from scripts.inputs import Inputs
from scripts.outputs import Outputs
from scripts.refactoring import Refactoring


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
        return {
            'source_file': 'README',
            'category': self.category,
            'title': self.title,
            'refactorings': [x for x in self.refactorings],
            'refactorings_and_titles': zip(self.refactorings, self.titles)
        }
