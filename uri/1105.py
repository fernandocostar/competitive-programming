b, n = map(int, input().split(" "))
while(b + n):
	bancos = [int(x) for x in input().split(" ")]
	for i in range(n):
		linha = [int(x) for x in input().split(" ")]
		bancos[linha[0]-1] -= linha[2]
		bancos[linha[1]-1] += linha[2]
	for each in bancos:
		if each < 0:
			bancos[0] = -1
			break
	if bancos[0] == -1:
		print("N")
	else:
		print("S")
	b, n = map(int, input().split(" "))
