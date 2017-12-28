def mean(vet):
	return sum(vet)//3
def eye(vet):
	return int(vet[0]*0.3+ 0.59*vet[1]+ vet[2]*0.11)

n = int(input())
for i in range(n):
	print("Caso #{}: ".format(i+1), end="")
	op = input()
	linha = [int(x) for x in input().split(" ")]
	if op == "min":
		print(min(linha))
	elif op == "max":
		print(max(linha))
	elif op == "mean":
		print(mean(linha))
	else:
		print(eye(linha))