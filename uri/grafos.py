m = int(input())
mat = []
aux = []

def solve(mat):
	cont = 0
	

for i in range(m):
	for n in range(m):
		aux.append(0)
	mat.append(aux)
	aux = []

a, b = map(int, input().split(" "))
while(a + b != 0):
	mat[a][b] = 1
	a, b = map(int, input().split(" "))

cont = 0




