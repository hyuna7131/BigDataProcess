#!/usr/bin/python3

try:
	f = open("input.txt", "rt")
	nf = open("output.txt", "wt")

	text = ""
	while True:
		row = f.readline()
		if not row: break
		text += row.upper()
	
	nf.write(text)

except FileNotFoundError:
	printf("파일이 없습니다.")
finally:
	f.close()
	nf.close()

