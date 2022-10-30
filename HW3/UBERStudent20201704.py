#!/usr/bin/python3

import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

from datetime import date

date_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
result_list = []

with open(input_file, 'rt') as f:
	for line in f:	
		str_arr = line.split(',')
		
		str_date = str_arr[1].split('/')
		year = int(str_date[2])
		month = int(str_date[0])
		day = int(str_date[1])

		result_list.append(str_arr[0].strip() + ',' + date_list[date(year, month, day).weekday()].strip() + ' ' + str(str_arr[2].strip()) + ',' + str(str_arr[3].strip()))
	
	with open(output_file, 'wt') as of:
		for element in result_list:
			of.write(element + "\n")
