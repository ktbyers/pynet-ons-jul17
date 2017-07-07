import yaml

yaml_file = "my_file.yml"
with open(yaml_file) as f:
    output = yaml.load(f)

print output

