n = int(input())
sobras = movimentos = 0
blocos = [int(x) for x in input().split(" ")]
soma = sum(blocos)
ultimo = (((2*soma)/n)+(n-1))//2 
primeiro = 1 + ultimo - n
for i in range(n):
	sobras += blocos[i] - (i+primeiro)
	if blocos[i] > i+primeiro:
		movimentos += blocos[i] - (i+primeiro) #se for possivel fazer a escada nunca entraremos aqui
print(-1) if sobras != 0 else print(int(movimentos))