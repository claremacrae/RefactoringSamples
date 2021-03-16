from scripts.file_from_template import FileFromTemplate
from scripts.outputs import Outputs


class OutputFiles:
    def __init__(self):
        self.files = []

    def add_source_file(self, inputs):
        template = FileFromTemplate(inputs, Outputs.source_file())
        self.files.append(template)

    def add_docs_file(self, inputs):
        template = FileFromTemplate(inputs, Outputs.doc_file())
        self.files.append(template)