while(True):
	try:
		user = input()
		new = ""
		for each in user:
			actual = ord(each)
			if actual >= 65 and actual <= 90 and actual >= 97 and actual <= 122:
				actual += 13
				new += chr(actual)
			else:
				new += each
		print(new)
	except EOFError:
		break