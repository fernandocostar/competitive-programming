j, r = map(int, input().split(" "))
pontos = [int(x) for x in input().split(" ")]
jogadores = []
for _ in range(j):
	jogadores.append(0)
for i in range(r):
	for k in range(j):
		jogadores[j] += pontos[(r*3)+j]
print(jogadores)
