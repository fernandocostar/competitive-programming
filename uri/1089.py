def solve(vet):
	count = 0
	vet += [vet[0], vet[-1]]
	keep = []
	ASCENDING = 1
	DESCENDING = -1
	status = 0 #-1 descending / 1 ascending
	for i in range(len(vet)-1):
		if vet[i] < vet[i+1] and status == DESCENDING:
			count += 1
			status = ASCENDING
			keep.append(-1)
		elif vet[i] > vet[i+1] and status == ASCENDING:
			count += 1
			status = DESCENDING
			keep.append(1)
		if vet[i] < vet[i+1]:
			status = ASCENDING
		elif vet[i] > vet[i+1]:
			status = DESCENDING
	count -= 1 if keep[0] == keep[-1] else 0
	return count  

t = int(input())
while(t != 0):
	data = [int(x) for x in input().split(" ")]
	print(solve(data))
	t = int(input())
