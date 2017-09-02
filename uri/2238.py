import math
from collections import deque

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




a, b, c, d = map(int, input().split(' '))
ans = -1
for n in divisors(c):
	if n % a == 0 and n % b > 0 and c % n == 0 and d % n > 0:
		ans = n
		break
print(ans)