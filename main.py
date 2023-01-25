import glob
import os
import yaml

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("./template"))

template = env.get_template('base.html.tmp')

all_path = glob.glob('./func/*/*.yaml')
all_link = []
for path in all_path:
    name = path.split('/')[-1].replace('.yaml', '')
    category = path.split('/')[-2]
    all_link.append(
        {
            'name': name,
            'url': f'../{category}/{name}.html'
        }
    )

for path in all_path:
    name = path.split('/')[-1].replace('.yaml', '')
    category = path.split('/')[-2]
    with open(path, 'r') as f:
        var = yaml.safe_load(f)
    var['all_link'] = all_link
    output = template.render(var)
    output_path = f'./html/{category}'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(f'{output_path}/{name}.html', 'w') as f:
        f.write(output)
