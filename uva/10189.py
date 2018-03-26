def checkAdjacent(mat, x, y):
	cont = 0
	xc = [1, 1, 1, 0, 0, -1, -1, -1]
	yc = [0, 1, -1, 1, -1, 1, 0, -1]
	for i in range(8):
		try:
			if mat[y+yc[i]][x+xc[i]] == "*":
				cont += 1
		except IndexError:
			pass
	return cont
f = 1
a, b = map(int, input().split(" "))
while(a+b):
	print("Field #{}:".format(f))
	mat = []
	for i in range(a):
		mat.append([x for x in input()])

	for i in range(a):
		for j in range(b):
			if mat[i][j] != "*":
				mat[i][j] = str(checkAdjacent(mat, j, i))

	for i in range(a):
		print("".join(mat[i]))
	f += 1
	a, b = map(int, input().split(" "))
	if(a+b):
		print("")

	