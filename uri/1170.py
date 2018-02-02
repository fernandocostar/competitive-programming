from math import log, ceil
n = int(input())
for i in range(n):
	v = float(input())
	print(ceil(log(v, 2)), "dias")