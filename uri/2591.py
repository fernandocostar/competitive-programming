n = int(input())
for i in range(n):
	word = input()
	totall = 0
	totalr = 0
	word = word.split("k")
	for each in word[0]:
		if each == "a":
			totall += 1
	for each in word[1]:
		if each == "a":
			totalr += 1
	word = "k"+"".join(["a" for i in range(totalr*totall)])
	print(word)