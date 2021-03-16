class Outputs:
    def __init__(self, directory_template):
        self.directory_template = directory_template
        self.file_name_template = '{{ data.source_file }}.{{ extension }}'

    @staticmethod
    def source_file():
        return Outputs('../RefactoringSamples/{{ stage }}/{{ data.category }}')

    @staticmethod
    def doc_file():
        return Outputs('../docs/{{ data.category }}/mdsource')