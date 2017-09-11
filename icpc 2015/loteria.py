n, k = map(int, input().split(" "))
mat = []
somas  = []
par = 0
impar = 0
for i in range(n):
	mat += [[int(x) for x in input().split(" ")]]
for each in mat:
	soma = sum(each)
	if soma % 2 == 0:
		par += 1
	else:
		impar += 1
	somas.append(sum(each))
if n == 1:
	print("S") if par == 1 else print("N")
else:
	if n % 2 == 0:
		if impar == par:
			print("N")
		else:
			print("S")
	else:
		if (impar-1) == par:
			print("N")
		else:
			print("S")


