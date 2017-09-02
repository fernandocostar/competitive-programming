def solve(a, b):
	s1 = set(a)
	s2 = set(b)
	final = set(list(set(a))+list(set(b)))
	return min(len(final)-len(s1), len(final)-len(s2))
p, s = map(int, input().split(" "))
while(p + s != 0):
	a = [x for x in input().split(" ")]
	b = [x for x in input().split(" ")]
	print(solve(a, b))
	p, s = map(int, input().split(" "))

