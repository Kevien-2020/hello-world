"""World Population"""

import json
import os

from pygal_maps_world.maps import World
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

filename = 'population_data.json'
filepath = os.path.dirname(__file__) + '/json/' + filename
openfile = open(filepath)

# with open(os.path.join(sys.path[0], filename), "r") as f:
with openfile as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

WM_style = RS('#336699', base_style=LCS)
WM = World(style=WM_style)
WM.title = 'World Population in 2010, by Country'
WM.add('0-10m', cc_pops_1)
WM.add('10m-1bn', cc_pops_2)
WM.add('>1bn', cc_pops_3)

SAVE_PATH = os.path.realpath(os.path.dirname(__file__)) + "\\svg"
WM.render_to_file(os.path.join(SAVE_PATH, 'world_population.svg'))
