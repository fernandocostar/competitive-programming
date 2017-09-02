y, x = map(int, input().split(" "))
matriz = []
aux = []
for _ in range(y):
	matriz += [input()]	
y_new, x_new = map(int, input().split(" "))
y_new //= y
x_new //= x
printar = ""
for line in matriz:
	for n in range(y_new):
		for each in line:
			for k in range(x_new):
				printar += each
		print(printar)
		printar = ""

