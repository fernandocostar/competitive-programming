text = input()
while(text != "*"):
	text = text.split(" ")
	flag = True
	first = text[0][0]
	for each in text:
		if first.upper() != each[0].upper():
			flag = False
			break
	print("Y") if flag else print("N")
	text = input()