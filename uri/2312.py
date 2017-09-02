times = int(input())
quadro = []


for _ in range(times):

	user = input().split(" ")
	aux = [int(user[1]), int(user[2]), int(user[3]), user[0]]
	quadro.append(aux)

quadro = sorted(quadro, reverse=True)
for each in quadro:
	print(each[3], each[0], each[1], each[2])