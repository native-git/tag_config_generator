#!/usr/bin/env python

size = 193.0

x_offset = 914.4
y_offset = 914.4

x_dim = 21
y_dim = 22

total = x_dim * y_dim

with open('final_grid.yml', 'a') as f:
	f.write('%YAML:1.0\n')
	f.write('\n')
	f.write('ceiling_grid_razpi:\n')
	for tag in range(0,total):
		
		y_coord = tag % y_dim
		x_coord = (tag - y_coord) / y_dim

		if x_coord == 20:
			z = '0.'
		else:
			z = '0.'

		x = x_coord * x_offset
		y = y_coord * y_offset

		translation = '[' + str(x) + ', ' + str(y) + ', ' + str(z) + ']'

		
		f.write('  - tag: ' + str(tag) + '\n')
		f.write('    size: ' + str(size) + '\n')
		f.write('    translation: ' + translation + '\n')
		f.write('    keep: false\n')