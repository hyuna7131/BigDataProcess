#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

genre_dict = dict()

with open(input_file, "rt") as f:	
	for line in f:
		str_arr = line.split('::')
		str_arr2 = str_arr[2].split('|')
		
		for element in str_arr2:
			if element not in genre_dict:
				genre_dict[element.strip()] = 1
			else:
				genre_dict[element.strip()] += 1
				
	genre = genre_dict.keys()
	count = genre_dict.values()
	with open(output_file, 'w') as of:
		for key, value in zip(genre, count):		
			of.write(key + " " + str(value) + "\n")
