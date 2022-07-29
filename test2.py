import yaml
import pprint as pp

with open('test4.yml','r') as files:
    parse = yaml.safe_load(files)

#pp.pprint(parse['person']['details'])
#pp.pprint(parse['person3'])
#a = input("Enter, what you want to extract : \n")
#pp.pprint(parse[a])
pp.pprint(parse['employees2'])