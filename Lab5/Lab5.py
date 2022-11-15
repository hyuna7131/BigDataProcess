#!/usr/bin/python3

#Q1
color = {'빨':'red', '주':'orange', '노':'yellow', '초':'green', '파':'blue', '남':'navy', '보':'purple'}

print(color.get('초'))

#Q2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

dic = {
	a[0] :b[0],
	a[1] :b[1],
	a[2] :b[2],
	a[3] :b[3],
	a[4] :b[4],
	a[5] :b[5],
	a[6] :b[6],
	a[7] :b[7],
	a[8] :b[8],
	a[9] :b[9]
}

print(dic[6])

#Q3
price = [10000, 8000, 7500, 12000, 25000]

for i in range(len(price)):
	print(float(price[i])*0.8, end=',')
print()

#Q4

from_dict = dict()
file = input('Enter file name : ')

with open(file, "rt") as fp:
	for line in fp:
		if line.startswith("From"):
			str_arr = line.split()
			if str_arr[1] not in from_dict:
				from_dict[str_arr[1]] = 1
			else:
				from_dict[str_arr[1]] += 1
print(from_dict)
	
#Q5

import json

total = 0
with open("movie.json", "rt") as fp:
	json_data = json.load(fp)
	
	movie_list = json_data["movie"]
	
	for item in movie_list:
		salesAmt = int(item["salesAmt"])
		
		total+= salesAmt
		
print("오늘 매출액은 총 " + str(total) + "원")

