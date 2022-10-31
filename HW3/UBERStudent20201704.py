#!/usr/bin/python3

import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

from datetime import date

date_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
result_dic = dict()

with open(input_file, 'rt') as f:
	for line in f:	
		str_arr = line.split(',')
		str_arr[3] = str_arr[3].strip()
		
		str_date = str_arr[1].split('/')
		year = int(str_date[2])
		month = int(str_date[0])
		day = int(str_date[1])

		week_num = date_list[date(year, month, day).weekday()]
		
		region_day = str_arr[0]+','+week_num
		
		
		if region_day not in result_dic:
			result_dic[region_day] = [int(str_arr[2]), int(str_arr[3])]
		else:
			for i in result_dic:
				if i == region_day:
					result_dic[region_day][0] += int(str_arr[2])
					result_dic[region_day][1] += int(str_arr[3])
		
	##key = result_dic.keys()
	##a = list(result_dic.)
	##value = result_dic.items()
	with open(output_file, 'wt') as of:
		for key1, value1 in result_dic.items():
			of.write(key1 + " " + str(value1[0]) + ',' + str(value1[1]) + "\n")
