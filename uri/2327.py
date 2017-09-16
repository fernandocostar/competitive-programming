n = int(input())
def solve(n):
	colunas = [0]*n
	r = 0
	diag1 = 0
	diag2 = 0
	j = 0
	for i in range(n):
		linha = [int(x) for x in input().split(" ")]
		diag1 += entrada[j]
		diag2 += entrada[len(entrada)-1-j]
		if sum(linha) != r and i != 0:
			r = -1
		r = sum(linha)
		for j in range(n):
			colunas[j] += linha[j]
		j += 1
	if r != diag1 or r != diag2:
		r = -1
	for each in colunas:
		if each != r:
			r = -1
	return r
print(solve(n))
#input do uri tá bugado