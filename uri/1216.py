soma = 0
total = 0
while(True):
	try:
		name = input()
		soma += float(input())
		total += 1
	except 	EOFError:
		break
soma = round(soma/total, 1)
print(soma)