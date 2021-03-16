import os

from jinja2 import Template

from scripts.constants import do_not_overwrite


class FileFromTemplate(object):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def create_file(self, refactoring, env):
        output_directory = self.render_file_template(env, refactoring, self.outputs.directory_template)
        os.makedirs(output_directory, exist_ok=True)
        output_file = self.render_file_template(env, refactoring, self.outputs.file_template)
        output_file2 = self.render_string_template(refactoring, self.outputs.file_name_template)
        if output_file2 != output_file:
            print(output_file)
            print(output_file2)
            print("Error")
        output_file_name = os.path.join(output_directory, output_file)

        self.expand_template(env, output_file_name, refactoring)

    def expand_template(self, env, output_file_name, refactoring):
        output = self.render_file_template(env, refactoring, self.inputs.template_name)
        self.write_file(output, output_file_name)

    def write_file(self, output, output_file_name):
        if os.path.exists(output_file_name) and self.inputs.overwrite_if_existing == do_not_overwrite:
            print(f'File already exists: not overwriting: {output_file_name}')
            return
        with open(output_file_name, 'w') as f:
            f.write(output)

    def render_file_template(self, env, refactoring, template_name):
        template = env.get_template(template_name)
        return self.render_template(refactoring, template)

    def render_string_template(self, refactoring, template_text):
        template = Template(template_text)
        return self.render_template(refactoring, template)

    def render_template(self, refactoring, template):
        return template.render(data=refactoring, extension=self.inputs.extension, stage=self.inputs.stage)