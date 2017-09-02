while(True):
	try:
		instructions = input()
		max_read = int(input())
		count = 0
		actual = 0
		for each in instructions:
			if each == "R":
				actual += 1
			if actual == max_read:
				count += 1
				actual = 0
			if each == "W":
				count += 1
				if actual > 0:
					count += 1
					actual = 0
		if actual > 0:
			count += 1
		print(count)  
	except EOFError:
		break