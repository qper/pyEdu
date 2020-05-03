from yaml import dump, load, FullLoader
from jinja2 import Environment, FileSystemLoader

yaml_data = {}
with open(r'yaml/main.yml') as file:
    yaml_data = load(file, Loader=FullLoader)

# print(dump(yaml_data))

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('index.html.j2')

output = template.render(data=yaml_data['person'])
print(output)
