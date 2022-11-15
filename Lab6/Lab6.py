#!/usr/bin/python3
#Q1

from math import sqrt as sq

height = 5
base = 8
hypotenuse = sq(height **2 + base **2)

print(hypotenuse)

#Q2

import datetime

today = datetime.date.today()
birth = datetime.date(1994, 5, 5)

print(today - birth)

#Q3

import random

for i in range(10):
	print(random.randint(10, 20+1))

#Q4

str_line = input("숫자 두개를 입력하세요: ")

int_arr = list(map(lambda x:int(x), str_line.split()))

try:
	print(int_arr[0]/int_arr[1])
except ZeroDivisionError:
	print("division by zero")
	
	
