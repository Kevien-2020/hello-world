"""Bar Descriptions"""

import os
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333344', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie'}, 
    {'value': 15028, 'label': 'Description of django'}, 
    {'value': 14798, 'label': 'Description of flask'}
    ]

chart.add('', plot_dicts)
SAVE_PATH_SVG = os.path.realpath(os.path.dirname(__file__)) + "\\svg"
chart.render_to_file(os.path.join(SAVE_PATH_SVG, 'bar_descriptions.svg'))
