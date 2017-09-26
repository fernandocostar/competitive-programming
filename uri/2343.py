n = int(input())
matriz = [[0]*500 for i in range(500)]
toggle = 1
for _ in range(n):
	x, y = map(int, input().split(" "))
	matriz[y][x] += 1
	if matriz[y][x] > 1:
		print(1)
		toggle = 0
		break
print(sum([len(x) for x in matriz]))
if toggle == 1:
	print(0)