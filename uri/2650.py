t, m = map(int, input().split(" "))
for i in range(t):
	l = input().split(" ")
	if int(l[-1]) > m:
		print(" ".join(l[:-1]))