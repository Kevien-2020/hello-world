"""World Population"""

import json
import os

# location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


'''
location = os.path.realpath(os.path.dirname(__file__)) + "\csv"

print('\n' + location + '\n')

openfile = open(os.path.join(location, 'population_data.json'), encoding="utf8")


with openfile as f:
    pop_data = json.load(f)


'''

'''
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), "/json"))
print('\n' + location + '\n')
openfile = open(os.path.join(location, 'population_data.json'), encoding="utf8")

'''

'''
full_path = os.path.join(os.path.dirname(__file__), '\json\population_data.json')

print(full_path + '\n')

openfile = open(full_path, encoding="utf8")
'''


filePath = os.path.dirname(__file__)+'/json/' + 'population_data.json'
fileDesc = open(filePath)

with fileDesc as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ": " + population)




'''
fileData = fileDesc.read()
fileDesc.close()
'''