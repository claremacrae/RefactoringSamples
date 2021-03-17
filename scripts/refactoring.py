from scripts.constants import do_not_overwrite, overwrite_if_exists
from scripts.helpers import remove_spaces
from scripts.inputs import Inputs
from scripts.output_files import OutputFiles
from scripts.outputs import Outputs


class Refactoring:
    templates = None

    def __init__(self, title):
        self.title = title

    def create_files(self, category_title):
        refactoring = self.as_dictionary(category_title)
        for f in Refactoring.templates.files:
            f.create_file(refactoring)

    def as_dictionary(self, category_title):
        return {
            'category': remove_spaces(category_title),
            'category_title': category_title,
            'source_file': remove_spaces(self.title),
            'title': self.title
        }

    @staticmethod
    def create_templates():
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


Refactoring.templates = Refactoring.create_templates()
