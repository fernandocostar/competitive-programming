x = [[1,1],[1,1]]
y = [[1,1],[1,1]]

x[0][0], y[0][0], x[0][1], y[0][1] = input().split(" ", 3)
x[1][0], y[1][0], x[1][1], y[1][1] = input().split(" ", 3)

for m in range(0, 2):
	for n in range(0, 2):
		x[m][n] = int(x[m][n])

for m in range(0, 2):
	for n in range(0, 2):
		y[m][n] = int(y[m][n])

print(0) if (x[0][1] < x[1][0]) or (x[1][1] < x[0][0]) or (y[0][1] < y[1][0]) or (y[1][1] < y[0][0]) or (x[0][0] > x[1][1]) or (x[1][0] > x[0][1]) or (y[0][0] > y[1][1]) or (y[1][0] > y[0][1]) else print(1)
