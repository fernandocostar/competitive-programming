while True:
	try:
		c, n = map(int, input().split())
		count  = 0
		estacionamento = [["L", c]]
		for i in range(n):
			l = input().split()
			if len(l) == 3:
				l[2] = int(l[2])
				for i in range(len(estacionamento)):
					if estacionamento[i][0] == "L" and estacionamento[i][1] >= l[2]:
						count += 10
						estacionamento.insert(i, [l[1], l[2]])
						if estacionamento[i+1][1] - l[2]: estacionamento[i+1][1] -= l[2]
						else: estacionamento.pop(i+1)
						break
			else:
				pilha = []
				estacionamento.append(["L", 0])
				for i in range(len(estacionamento)):
					if estacionamento[i][0] == l[1]: estacionamento[i][0] = "L"
				for i in range(len(estacionamento)): 
					if len(pilha) and estacionamento[i][0] == "L" and pilha[-1][0] == "L": pilha[-1][1] += estacionamento[i][1]
					else: pilha.append(estacionamento[i])
				estacionamento = pilha.copy()
		print(count)
	except EOFError: break