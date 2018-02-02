fats = [1]*22
ultimo = 1
for i in range(1, 22):
	fats[i] = fats[i-1]*i

while True:
	try:
		a, b = map(int, input().split(" "))
		print(fats[a] + fats[b])
	except EOFError:
		break