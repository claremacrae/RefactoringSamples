from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('../templates')
env = Environment(loader=file_loader)
template = env.get_template('refactoring-pattern.md')
output = template.render(Category='Extract', SourceNameBase = 'ExtractClass')
print(output)
