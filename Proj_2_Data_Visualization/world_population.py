"""World Population"""

import json
import os

from country_codes import get_country_code

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

# Load the data into a list.
filename = 'population_data.json'
openfile = open(os.path.join(
    __location__, 'population_data.json'), encoding="utf8")

# with open(os.path.join(sys.path[0], filename), "r") as f:

with openfile as f:
    pop_data = json.load(f)

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print('ERROR - ' + country_name)
