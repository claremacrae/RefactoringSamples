class Outputs:
    def __init__(self, directory_template):
        self.directory_template = directory_template
        self.file_name_template = '{{ data.source_file }}.{{ extension }}'
