user = int(input())
while(user != 0):
	words = []
	longest = 0
	aux = ""
	#input
	for i in range(user):
		words += [input()]
		if len(words[i]) > longest:
			longest = len(words[i])
	for i in range(user):
		if longest - len(words[i]) > 0:
			for k in range(longest - len(words[i])):
				aux += " "
			aux += words[i]
			print(aux)
		else:
			print(words[i])
		aux = ""
	print("\n")
	user = int(input())

