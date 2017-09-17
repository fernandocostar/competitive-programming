n = int(input())
t = 1
while(n!=0):
	somas = [0, 0]
	for k in range(n):
		a1, a2 = map(int, input().split(" "))
		somas[0] += a1
		somas[1] += a2
	print("Teste", t)
	print("Aldo\n") if somas[0] > somas[1] else print("Beto\n")
	n = int(input())
	t+=1