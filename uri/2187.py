bits = [50, 10, 5, 1]
result = []
n = int(input())
c = 1
while(n != 0):
	for i in range(4):
		result.append(n//bits[i])
		n = n%bits[i]
	print("Teste", c)
	print(*result, sep=" ")
	print("")
	result = []
	n = int(input())
	c += 1