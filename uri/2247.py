n = int(input())
t = 1
while(n != 0):
	actual = 0
	print("Teste", t)
	for k in range(n):
		a, b = map(int, input().split(" "))
		actual += (a-b)
		print(actual)
	print("")
	n = int(input())
	t += 1
