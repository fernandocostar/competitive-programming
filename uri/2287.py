def get_max(vetor):
	vetor_aux = set(vetor)
	maxx = 0
	resp = 0
	for i in vetor_aux:
		aux = vetor.count(i)
		if aux > maxx:
			resp = i
			maxx = aux
	return resp

d = {
	'A': [0, 1],
	'B': [2, 3],
	'C': [4, 5],
	'D': [6, 7],
	'E': [8, 9]
}

t = 1
n = int(input())
while(n != 0):
	lista = [[],[],[],[],[],[]]

	for m in range(n):
		entrada = [x for x in input().split(" ")]
		letras = entrada[10:17]
		i = 0
		for j in range(6):
			lista[i].append(entrada[d[letras[j]][0]])
			lista[i].append(entrada[d[letras[j]][1]])
			i += 1
	print("Teste", t)
	for l in lista:
		print("%s "%(get_max(l)), end="")
	print("\n")
	t += 1
	n = int(input())