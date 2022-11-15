#!/usr/bin/python3

#01
num = 0
sum = 0

while num < 200:
	num += 1
	if(num % 3) == 0:
		sum = sum + num
print(sum)
print( )

#02
for n in range(1, 10+1):
	if n % 3 != 0:
		print(n)
print( )

#03
for i in range(10):
	for k in range(10,i,-1):
		print(' ',end='')

	for k in range(i):
		print("* ",end='')
	print()
print( )

#04
for i in range(10):
	for k in range(10, i, -1):
		print(' ', end = '')
		
	for k in range((i+1)*2 - 1):
		print('*', end = '')
	print( )
print()

#05
def avg(a, b, c):
	return (a+b+c)/3
	
print(avg(1,3,5))
print(avg(2,3,4))
print(avg(1,6,9))
print( )

#06
def max(*a):
	max = a[0]
	for num in a:
		if max < num:
			max = num
	return max

print(max(1, 4, 6))
print(max(10, 5, 87, 57, 38))
print(max(4, 3, 2, 1))
print( )

#07
def fib(n):
	if n == 0:
		return 0
	elif n ==1 or n ==2:
		return 1
	else:
		return fib(n-1) + fib(n-2)	
		
print(fib(5))
print(fib(10))
print(fib(35))
print( )

#08
def fib_opt(m):
	F = [0 for m in range(m)]
	
	if m <= 2:
		return 1
	else:
		if F[m-1] == 0:
			F[m-1] = fib(m-1)
		
		if F[m-2] == 0:
			F[m-2] = fib(m-2)
		return F[m-1] + F[m-2]
	

print(fib_opt(5))
print(fib_opt(10))
print(fib_opt(35))
print( )
