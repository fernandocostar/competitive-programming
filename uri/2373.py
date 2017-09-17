n = int(input())
soma = 0
for _ in range(n):
	l, c = map(int, input().split(" "))
	if l > c:
		soma += c
print(soma)