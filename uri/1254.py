while True:
	try:
		b4 = input()
		after = input()
		t = input()
		print(t.replace(b4, after))
	except EOFError:
		break