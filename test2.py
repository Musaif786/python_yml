import yaml
import pprint as pp

with open('test2.yml','r') as files:
    parse = yaml.safe_load(files)

#pp.pprint(parse['person']['details'])
pp.pprint(parse['person'])