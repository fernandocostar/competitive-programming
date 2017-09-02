times = int(input())




for _ in range(times):
	number = int(input())
	not_allowed = []
	students = input().split(" ")
	status = input().split(" ")

	total = 0
	presences = 0

	for i in range(len(status)):
		for each in status[i]:
			if each == "P":
				total += 1
				presences += 1
			elif each == "A":
				total += 1
		if presences/total < 0.75:
			not_allowed += [students[i]]
		total = 0
		presences = 0
	print(" ".join(not_allowed))
