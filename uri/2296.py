n = int(input())
trilhas = []
for _ in range(n):
	trilha = [int(x) for x in input().split(" ")[1:]]
	reversa = list(reversed(trilha))
	dif = 0
	dif2 = 0
	for m in range(len(trilha)-1):
		calc1 = trilha[m+1] - trilha[m]
		calc2 = reversa[m+1] - reversa[m]
		if calc1 > 0:
			dif += calc1
		if calc2 > 0:
			dif2 += calc2
	trilhas.append(min(dif, dif2))
m = trilhas[0]
im = 1
for i in range(n):
	if m > trilhas[i]:
		im = i+1
		m = trilhas[i]
print(im)
