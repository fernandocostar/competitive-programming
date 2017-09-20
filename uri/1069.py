n = int(input())
for _ in range(n):
	status = 0
	count = 0
	areia = input()
	for each in areia:
		if each == "<":
			status += 1
		elif each == ">" and status != 0:
			count += 1
			status -= 1
	print(count)