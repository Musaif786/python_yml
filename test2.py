import yaml
import pprint as pp

with open('test2.yml','r') as f:
    parse = yaml.safe_load(f)

pp.pprint(parse['person']['details'])