n = int(input())
t = 1
while(n != 0):
	print("Teste", t)
	numbers = [int(x) for x in input().split(" ")]
	for i in range(len(numbers)):
		if (i+1) == numbers[i]:
			print(numbers[i])
	print("")
	t += 1
	n = int(input())