def solve(t, to, fr):
	text = t
	new = ""
	frlower = "".join([x.lower() for x in fr])
	tolower = "".join([x.lower() for x in to])

	frupper = "".join([x.upper() for x in fr])
	toupper = "".join([x.upper() for x in to])

	for each in text:
		if each in frlower
	return text




while(True):
	try:
		a, b = map(int, input().split(" "))
		to_replace = input()
		replace = input()
		for _ in range(b):
			user = input()
			print(solve(user, to_replace, replace))
	except EOFError:
		break