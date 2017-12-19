n = int(input())
while(n != 0):
	for i in range(n):
		resultado = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"}
		linha = [int(x) for x in input().split(" ")]
		linha = [i for i in range(5) if linha[i] <= 127]
		print("*") if len(linha) != 1 else print(resultado[linha[0]])
	n = int(input())