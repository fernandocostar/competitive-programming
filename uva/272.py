OPEN = 1
CLOSED = 0
flag = CLOSED
while True:
	try:
		t = input()
		r = ""
		for each in t:
			if each == "\"":
				if flag == CLOSED:
					r += "``"
					flag = OPEN
				else:
					r += "''"
					flag = CLOSED
			else:
				r += each
		print(r)
	except EOFError:
		break