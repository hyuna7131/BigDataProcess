#!/usr/bin/python3

with open('mbox-short.txt', 'r') as f:
	count =0
	sum = 0
	for line in f:
		if line.startswith('X-DSPAM-Confidence'):
			sp = line.find(':')
			sum += float(line[sp+1:])
			count += 1
	print(sum/count)
	
