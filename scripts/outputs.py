class Outputs:
    def __init__(self, directory_template, file_template):
        self.directory_template = directory_template
        self.file_template = file_template
        self.file_name_template = '{{ data.source_file }}.{{ extension }}'

    @staticmethod
    def source_file():
        return Outputs(directory_template='source-directory.txt', file_template='source-file.txt')

    @staticmethod
    def doc_file():
        return Outputs(directory_template='doc-directory.txt', file_template='doc-file.txt')