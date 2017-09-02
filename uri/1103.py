def solve(h1, m1, h2, m2):
	if h2 < h1 or (h1 == h2 and m2 < m1):
		return ((h2+24)*60 + m2) - (h1*60 + m1)
	else:
		return (h2*60 + m2) - (h1*60 + m1)

h1, m1, h2, m2 = map(int, input().split(" "))
while(h1+m1+h2+m2 != 0):
	print(solve(h1, m1, h2, m2))
	h1, m1, h2, m2 = map(int, input().split(" "))

