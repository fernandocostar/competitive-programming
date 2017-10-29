def solve(vet):
	cont = 0
	aux = [x for x in vet]
	aux = sorted(aux, reverse=True)
	for i in range(len(vet)):
		if vet[i] == aux[i]:
			cont += 1
	return cont
n = int(input())
for _ in range(n):
	k = int(input())
	vet = [int(x) for x in input().split(" ")]
	print(solve(vet))
