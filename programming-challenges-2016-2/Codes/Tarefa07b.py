import math

def retornaLados(diagonais):
    xa = ((3 + math.sqrt(9 + 8 * diagonais))/2)
    return int(math.ceil(xa))

user = int(input())

while(user != 0):
	print(retornaLados(user))
	user = int(input())
print("")