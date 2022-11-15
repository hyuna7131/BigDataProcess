#!/usr/bin/python3

try:
	f = open("mbox-short.txt", "rt")
	text = f.read()

	count =0
	sum = 0
	for line in f:
		if line.startswith('X-DSPAM-Confidence'):
			sp = line.find(':')
			sum += float(line[sp+1:])
			count += 1
	print(sum/count)

except FileNotFoundError:
	print("파일이 없습니다.")
finally:
	f.close()
	
	
	

