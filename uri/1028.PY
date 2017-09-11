import math
from collections import deque

t = int(input())

def divisors(n):
	d1 = deque()
	d2 = deque()
	for i in range(1, math.ceil(math.sqrt(n))):
		if n % i == 0:
			d1.append(i)
			d2.appendleft(int(n/i))
	s = math.sqrt(n)
	if n % s == 0: 
		return list(d1) + [int(math.sqrt(n))] + list(d2)
	else:
		return list(d1) + list(d2)

def mdc(m, n):
	minimo = min(m, n)
	maximo = max(m, n)
	result = 0
	divisores = divisors(minimo)
	for i in range(1, len(divisores)):
		if maximo%divisores[i] == 0:
			result = divisores[i]
	return result

for _ in range(t):
	m, n = map(int, input().split(" "))
	print(mdc(m, n))