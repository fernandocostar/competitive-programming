n = int(input())
ROUND = 1
while(n != 0):
	p = input()
	i = input()
	print("Teste", ROUND)
	for _ in range(n):
		n1, n2 = map(int, input().split(" "))
		print(p) if (n1 + n2) % 2 == 0 else print(i)
	print()
	n = int(input())
	ROUND += 1