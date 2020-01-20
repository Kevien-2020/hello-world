"""NA Populations"""

import os
from pygal_maps_world.maps import World

WM = World()
WM.title = 'Populations of Countries in North America'
WM.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

SAVE_PATH = os.path.realpath(os.path.dirname(__file__)) + "\\svg"
WM.render_to_file(os.path.join(SAVE_PATH, 'na_populations..svg'))
