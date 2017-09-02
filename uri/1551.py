times = int(input())
for _ in range(times):
	result = []
	user = input()
	user = user.replace(",", "")
	user = user.replace(" ", "")
	for char in user:
		if char not in result:
			result += [char]
	tam = len(result)
	if tam == 26:
		print("frase completa")
	elif tam >= 13:
		print("frase quase completa")
	else:
		print("frase mal elaborada")


