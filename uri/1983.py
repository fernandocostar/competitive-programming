k = int(input())
n = []
aux = []
for i in range(k):
	l = input().split(" ")
	aux.append(float(l[1]))
	aux.append(int(l[0]))
	n.append(aux)
	aux = []
n.sort(reverse=True)
if n[0][0] < 8:
	print("Minimum note not reached")
else:
	print(n[0][1])