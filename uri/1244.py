def solve(vet):
	for i in range(len(vet)-1):
		for j in range(len(vet)-1):
			if len(vet[j]) < len(vet[j+1]):
				aux = vet[j]
				vet[j] = vet[j+1]
				vet[j+1] = aux

n = int(input())

strings = []

for i in range(n):
	strings = input().split(" ")
	solve(strings)
	print(*strings)