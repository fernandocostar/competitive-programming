n = int(input())
for i in range(n):
	flag = False
	k = int(input())
	k = 2015 - k
	if k <= 0:
		k -= 1
		k = -k
		flag = True
	print(k, "D.C.") if not flag else print(k, "A.C.")
