n = int(input())
t = 1
while( n != 0):
	notas = []
	alunos = []
	result = []
	for _ in range(n):
		a, no = map(int, input().split(" "))
		notas.append(no)
		alunos.append(a)
	maximo = max(notas)
	print("Turma", t)
	for i in range(n):
		if notas[i] == maximo:
			result.append(str(alunos[i]))
	print(" ".join(result)+" ")
	print("")
	t += 1
	n = int(input())