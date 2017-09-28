n = int(input())
carta = 0
cartas = [0]*100100

ent = [int(x) for x in input().split(" ")]
for i in range(n):
	carta = ent[i]
	cartas[carta - 1] = i
rod = 1
for i in range(n-1):
	if cartas[i] > cartas[i+1]:
		rod += 1
print(rod, "")