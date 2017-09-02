t = int(input())
d = {}
for _ in range(t):
	l = input()
	p = input()
	d[l] = p
t = int(input())
for _ in range(t):
	n = input()
	l = input()
	print(n)
	print(d[l]+"\n")
