def calc(num):
	result = 1
	for i in range(1, num + 1):
		result *= 2*i
	return result

def solve(dado):
	pares = 0
	avulsos = 0

	for i in range(0, len(dado)-1, 2):
		if dado[i] == "*" and dado[i+1] == "*":
			pares += 1
		elif dado[i] == "*" and dado[i+1] != "*":
			avulsos += 1
		elif dado[i+1] == "*" and dado[i] != "*":
			avulsos += 1
	if pares == 0 and avulsos != 0:
		return 1
	
	pares = calc(pares)
	return pares


c = int(input())
dado = []

for _ in range(c):

	dado.append(input())
	aux = [x for x in input().split(" ")]
	dado.append(input())
	dado += [aux[0],aux[2],aux[1],aux[3]]
	print(solve(dado))
	dado = []