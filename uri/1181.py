line = int(input())
matriz = []
aux = []
op = input()
for y in range(12):
	for x in range(12):
		aux += [int(input())]
	matriz += [aux]
	aux = []
print(sum(matriz[line])) if op == "S" else print("%.2f"%(sum(matriz[line])/12))