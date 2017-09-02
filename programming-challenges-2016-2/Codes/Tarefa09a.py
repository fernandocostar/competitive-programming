t = int(input())

for k in range(t):
	recebendo = [int(n) for n in input().split(" ")]

	matriz = []

	for m in range(recebendo[0]):
		aux = []
		for n in range(recebendo[0]):
			aux += [0]
		matriz += [aux]

	print(matriz)

	for m in range(recebendo[1]):
		linha = input().split(" ")
		matriz[int(linha[0])-1][int(linha[1])-1] = 1

	print(matriz)