import os

from jinja2 import Template, FileSystemLoader, Environment

from scripts.constants import do_not_overwrite
from scripts.inputs import Inputs
from scripts.outputs import Outputs


class FileFromTemplate(object):
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)

    def __init__(self, inputs: Inputs, outputs: Outputs):

        self.inputs = inputs
        self.outputs = outputs

    def create_file(self, refactoring):
        output_directory = self.render_string_template(refactoring, self.outputs.directory_template)
        os.makedirs(output_directory, exist_ok=True)
        output_file = self.render_string_template(refactoring, self.outputs.file_name_template)
        output_file_name = os.path.join(output_directory, output_file)

        self.expand_template(output_file_name, refactoring)

    def expand_template(self, output_file_name, refactoring):
        output = self.render_file_template(refactoring, self.inputs.template_name)
        self.write_file(output, output_file_name)

    def write_file(self, output, output_file_name):
        if os.path.exists(output_file_name) and self.inputs.overwrite_if_existing == do_not_overwrite:
            print(f'File already exists: not overwriting: {output_file_name}')
            return
        with open(output_file_name, 'w') as f:
            f.write(output)

    def render_file_template(self, refactoring, template_name):
        template = FileFromTemplate.env.get_template(template_name)
        return self.render_template(refactoring, template)

    def render_string_template(self, refactoring, template_text):
        template = Template(template_text)
        return self.render_template(refactoring, template)

    def render_template(self, refactoring, template):
        return template.render(data=refactoring, extension=self.inputs.extension, stage=self.inputs.stage)