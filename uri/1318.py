n, m = map(int, input().split(" "))
while(n + m != 0):
	try:
		entry = [int(x) for x in input().split(" ")]
	except Exception:
		entry = []
	count = 0
	new = []
	repeat = []
	for each in entry:
		if each not in new:
			new += [each]
		else:
			if each not in repeat:
				repeat += [each]
	print(len(repeat))
	n, m = map(int, input().split(" "))
