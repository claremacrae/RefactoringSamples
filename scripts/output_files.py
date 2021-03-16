from scripts.file_from_template import FileFromTemplate
from scripts.outputs import Outputs


class OutputFiles:
    def __init__(self):
        self.files = []

    def add_docs_file(self, inputs):
        self.add_file(inputs, Outputs.doc_file())

    def add_file(self, inputs, outputs):
        template = FileFromTemplate(inputs, outputs)
        self.files.append(template)