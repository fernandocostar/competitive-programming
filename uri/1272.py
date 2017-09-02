times = int(input())
for _ in range(times):
	hidden = ""
	user = input()
	flag = True
	for char in user:
		if char != " " and flag:
			hidden += char
			flag = False
		elif char == " " and not flag:
			flag = True
	print(hidden)


