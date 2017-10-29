n = int(input())
contidos = [x for x in range(n)]
entrada = [int(x) for x in input().split(" ")]
for each in entrada:
	contidos[each-1] = -1
for each in contidos:
	if each != -1:
		print(each+1)
		breakbin