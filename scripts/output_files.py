from scripts.file_from_template import FileFromTemplate


class OutputFiles:
    def __init__(self):
        self.files = []

    def add_file(self, inputs, outputs):
        template = FileFromTemplate(inputs, outputs)
        self.files.append(template)