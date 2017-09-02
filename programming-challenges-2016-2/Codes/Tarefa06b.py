import math as mt

def retornaLados(diagonais):
	xa = ((3 + mt.sqrt(9 + 8 * diagonais))/2)
	xb = ((3 - mt.sqrt(9 + 8 * diagonais))/2)
    if xa > 0:
    	return math.ceil(xa)
    else:
    	return math.ceil(xb)


user = int(input())

while(user != 0):
	print(retornaLados(user))
	user = int(input())
