t = int(input())
for _ in range(t):
	x, y = map(int, input().split(" "))
	if y > x:
		print(2)
	else:
		print(x/y + (0 if x % y == 0 else 1))