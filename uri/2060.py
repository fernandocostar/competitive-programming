n = int(input())
qtd = [0, 0, 0, 0]
l = [int(x) for x in input().split(" ")]
for each in l:
	for i in range(4):
		if each % (i+2) == 0:
			qtd[i] += 1
for i in range(4):
	print(qtd[i], "Multiplo(s) de", i+2)
