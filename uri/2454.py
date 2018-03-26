a, b = map(int, input().split(" "))
if not a:
	print("C")
elif a and not b:
	print("B")
else:
	print("A")