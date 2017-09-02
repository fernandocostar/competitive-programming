t = int(input())
aux = []
aux2 = []
for _ in range(t):
	i =int(input())
	aux += [i]
	if i not in aux2:
		aux2 += [i]
aux2 = sorted(aux2)
for each in aux2:
	print("{} aparece {} vez(es)".format(each, aux.count(each))) 
