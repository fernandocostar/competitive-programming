n, k = map(int, input().split())
while(n+k):
	pilha = []
	flag = True
	for j in range(n):
		e, s = map(int, input().split())
		while(len(pilha) and pilha[-1][1] <= e):
			pilha.pop()
		if len(pilha) == 0:
			pilha.append([e, s])
		elif len(pilha) < k and s <= pilha[-1][1]:
			pilha. append([e, s])
		else: flag = False
	print("Sim") if flag else print("Nao")
	n, k = map(int, input().split())