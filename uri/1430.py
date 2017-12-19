ints = {"W":64, "H":32, "Q":16, "E":8, "S":4, "T":2, "X":1}
jingle = input()
while(jingle != "*"):
	corretos = 0
	total = 0
	for each in jingle:
		if each == "/" and total % 64 == 0 and total//64 == 1:
			corretos += 1
			total = 0
		elif each != "/":
			total += ints[each]
		else:
			total = 0
	print(corretos)
	jingle = input()