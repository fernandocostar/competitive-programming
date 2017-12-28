d = {}
while True:
	try:
		joia = input()
		if joia not in d:
			d[joia] = 1
		else:
			d[joia] += 1
	except EOFError:
		break
print(len(d.keys()))