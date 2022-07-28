import yaml

with open("test.yaml") as file:
    msg = yaml.load(file, Loader=yaml.Loader)
    print(msg)
