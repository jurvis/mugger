#!/usr/bin/env python

import os
import json
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def path_to_dict(path):
	d = {'name': os.path.basename(path)}
	if os.path.isdir(path):
		d['type'] = 'directory'
		d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
	else:
		d['type'] = "file"
	return d

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
	modules = []

	filetreeJSON = path_to_dict('./modules')
	for t in filetreeJSON['children']:
		if t['type'] == "directory":
			newDict = {'name': t['name'], 'files' : []}
			for f in t["children"]:
				if f['type'] == "file":
					newDict['files'].append(f['name'])
			modules.append(newDict)

	print modules

	fname = "index.html"
	context = {
		'modules': modules
	}
    #
	with open(fname, 'w') as f:
		html = render_template('index.html', context)
		f.write(html)




def main():
    create_index_html()

########################################

if __name__ == "__main__":
    main()
