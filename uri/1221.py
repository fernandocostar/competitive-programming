from math import sqrt, ceil

n = int(input())
for i in range(n):
	v = int(input())
	flag = 0
	if v == 0 or v == 1:
		print("Not Prime")
	else:
		for i in range(2, ceil(sqrt(v))):
			if v % i == 0:
				print("Not Prime")
				flag = 1
				break
		if not flag:
			print("Prime")