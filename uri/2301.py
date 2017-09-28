p, r = map(int, input().split(" "))
t = 1
while(p + r != 0):
	status = [int(x) for x in input().split(" ")]
	for k in range(r):
		rodada = [int(x) for x in input().split(" ")]
		correto = rodada[1]
		for i in range(rodada[0]):
			if rodada[i+2] != correto:
				status[i] = -1
		status = [x for x in status if x != -1]
	print("Teste", t)
	print(status[0])
	print("")
	t += 1
	p, r = map(int, input().split(" "))