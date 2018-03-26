n = int(input())
c = [1, 3, 5, 10, 25, 50, 100, 100000000]
for i in range(len(c)):
	if n > c[i]:
		pass
	else:
		print("Top", c[i])
		break