n = int(input())
for _ in range(n):
	l = [int(x) for x in input().split(" ")]
	c = l[1]
	r = 0
	while(c):
		if l[0] % 2:
			r += l[0]
			c -= 1
		l[0] += 1
	print(r)