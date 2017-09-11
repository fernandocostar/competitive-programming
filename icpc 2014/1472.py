def calcula(array):


while(True):
	try:
		result = 0
		n = int(input())
		array = [int(x) for x in input().split(" ")]
		array += array
		total = []
		inicio = 0
		fim = len(array)
		aux = 0
		soma = sum(array)
		if soma % 3 != 0:
			print(soma)
		else:
			lado = soma/3
			for i in range() 

	except EOFError:
		break