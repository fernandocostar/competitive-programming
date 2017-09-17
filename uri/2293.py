l, c = map(int, input().split(" "))
linhas = [0]*l
colunas = [0]*c
for k in range(l):
	aux = [int(x) for x in input().split(" ")]
	for m in range(c):
		colunas[m] += aux[m]
	linhas[k] = sum(aux)
print(max(max(colunas), max(linhas)))