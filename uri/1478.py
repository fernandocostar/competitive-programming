user = int(input())
while(user != 0):
	array = [x for x in range(1, user + 1)]
	array += array
	p = ""
	for j in range(user):
		for i in range(0 + j, user+j):
			p += str(array[i])+" "
		print(p)
		p = ""
	user = int(input())