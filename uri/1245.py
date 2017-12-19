while(True):
	try:
		n = int(input())
		d = [0]*61
		e = [0]*61
		for i in range(n):
			linha = input().split(" ")
			if linha[1] == "D":
				d[int(linha[0])] += 1
			else:
				e[int(linha[0])] += 1
		total = 0
		for i in range(61):
			total += min(d[i], e[i])
		print(total)
	except EOFError:
		break