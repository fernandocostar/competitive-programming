a, v = map(int, input().split(" "))
t = 1
while(a+v != 0):
	total = [0]*a
	r = []
	m = 0
	for i in range(v):
		entrada = [int(x) for x in input().split(" ")]
		total[entrada[0]-1] += 1
		total[entrada[1]-1] += 1
	print("Teste", t)
	for j in range(a):
		if total[j] > m:
			m = total[j]
			r = [j+1]
		elif total[j] == m:
			r.append(j+1)
	print(*r, sep=" ", end=" \n")
	print("")
	t += 1
	a, v = map(int, input().split(" "))
