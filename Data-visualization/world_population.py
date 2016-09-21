
import json
from pygal_maps_world.i18n import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle
from country_codes import get_country_code



filename = "/Users/mahmutkilic/Desktop/PythonExamples/pcc-master/chapter_16/pygal2_update/population_data.json"


with open(filename) as f:
    pop_date = json.load(f)



cc_populations = {}
for pop_dict in pop_date:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 poplulation levels.

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop <10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm = World()
wm_style =RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1b', cc_pops_2)
wm.add('>1b', cc_pops_3)

wm.render_to_file('world_population.svg')
