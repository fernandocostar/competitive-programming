t = int(input())
for _ in range(t):
	user = [x for x in input()]
	if user[0] == user[2]:
		print(int(user[0])*int(user[2]))
	elif user[1] == user[1].upper():
		print(int(user[2])-int(user[0]))
	else:
		print(int(user[2])+int(user[0]))
