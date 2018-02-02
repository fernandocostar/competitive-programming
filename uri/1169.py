k = int(input())
for _ in range(k):
	soma = 0
	n = int(input())
	for i in range(n):
		soma += 2**i
	print(soma//12000, "kg")