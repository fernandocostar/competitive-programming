while True:
	try:
		t = input()
		flag = False
		new = ""
		for each in t:
			if each == "O" or each == "o" or each == "0":
				new += "0"
			elif each == "1" or each == "l":
				new += "1"
			elif ord(each) >= ord("0") and ord(each) <= ord("9"):
				new += each
			elif each == "," or each == " ":
				pass
			else:
				flag = True
		if len(new) == 0:
			flag = True
		if flag:
			print("error")
		elif int(new) > 2147483647:
			print("error")
		else:
			print(int(new))
	except EOFError:
		break