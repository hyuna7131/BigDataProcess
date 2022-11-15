#!/usr/bin/python3

#Q1
s = "universe"
for c in s:
	print(c, end='\n')
print()
	
#Q2
address = input('웹 주소를 입력하세요:')

if address.endswith(".kr"):
	print("한국 도메인입니다")
else:
	print("한국 도메인이 아닙니다")
print()
	
#Q3
sosi = "태연, 서현, 수영"
girls = sosi.split(',')
for girl in girls:
	print(girl.strip() + '사랑해', end = '\n')
print()
	
#Q3-1
str = "X-DSPAM-Confidence:0.8475"
num = str[str.find(':')+1:]
print(float(num))
print()

#Q4
s = "아침에 커피로 시작하고 밥 먹고 커피 마시고 자기 전에도 커피를 마신다"
print(s.replace("커피", "우유"))
print()

#Q5
num = "901231-1914983"

if num[7:8] == '1':
	print(num[0:2] +"년생 남자")
print()
	
#Q6
sum = 356
avg = 89.2785

print('%d, %.2f' %(sum, avg))
print()

#Q7
score = [88, 95, 70, 100, 99, 50, 70, 75]

sum = 0
for s in score:
	sum += s
print("sum = ", sum, ", avg = ", sum/len(score))
print()
	
#Q8
score = [88, 95, 70, 100, 99]
score[2] = 0
for s in score:
	print(s, end=',')
print('\n')
	
#Q9
nums = [n*2 for n in range(1, 50+1)]

for i in nums:
	print(i, end=',')
print('\n')
	
#Q10
for n in range(1, 10):
	if n%3 == 0:
		print(n*n, end=',')
print('\n')
		
#Q11
score_str = input('5개의 성적을 입력하세요(각 값은 공백으로 분리): ')

score_str = score_str.strip()

scores = score_str.split()

score_ints = [int(str_n) for str_n in scores]

score_ints.sort()
print(score_ints)
