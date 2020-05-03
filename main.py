import yaml

with open(r'yaml/main.yml') as file:
    print(yaml.dump(yaml.load(file, Loader=yaml.FullLoader)))
