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

resposta = []
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

	for l in lista:
		resposta.append(get_max(l))
	print("Teste", t)
	print("%s %s %s %s %s %s "%(resposta[0], resposta[1], resposta[2], resposta[3], resposta[4], resposta[5]))
	print()
	t += 1
	n = int(input())
	resposta = []