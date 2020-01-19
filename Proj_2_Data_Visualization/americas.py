"""Americas"""

import os
from pygal_maps_world.maps import World

WM = World()
WM.title = 'North, Central and South America'

WM.add('North America', ['ca', 'mx', 'us'])
WM.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
WM.add('South America', ['ar', 'bo', 'br', 'cl', 'co',
                         'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

SAVE_PATH = os.path.realpath(os.path.dirname(__file__)) + "\\svg"
WM.render_to_file(os.path.join(SAVE_PATH, 'americas.svg'))
