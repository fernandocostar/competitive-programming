fat = [1]
for i in range(1, 10):
	fat.append(fat[i-1]*i)
n = input()
while(n != "0"):
	soma = 0
	for i in range(len(n)):
		soma += int(n[-i-1])*fat[i+1]
	print(soma)
	n = input()