from math import sqrt

while True:
	try:
		n = abs(int(input()))
		half = n//2
		if sqrt(half)%1 == 0 or n%4 == 1:
			print("YES")
		else:
			print("NO")
	except EOFError:
		break
