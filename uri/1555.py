def ra(x, y):
	return (3*x)**2 + y**2

def be(x, y):
	return 2*(x**2) + (5*y)**2

def ca(x, y):
	return -100*x + y**3

n = int(input())
for i in range(n):
	x, y = map(int, input().split(" "))
	r = ra(x, y)
	b = be(x, y)
	c = ca(x, y)
	if(r > b and r > c):
		print("Rafael ganhou")
	elif(b > r and b > c):
		print("Beto ganhou")
	else:
		print("Carlos ganhou")
