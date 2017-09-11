j, r = map(int, input().split(" "))
pontos = [int(x) for x in input().split(" ")]
jogadores = []
m = 0
ma = 0
for _ in range(j):
	jogadores.append(0)
for i in range(r):
	for k in range(j):
		jogadores[k] += pontos[(i*j)+k]
		if jogadores[k] >= ma:
			m = k
			ma = jogadores[k]
print(m+1)	
