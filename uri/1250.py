t = int(input())
for i in range(t):
	count = 0
	n = int(input())
	l = [int(x) for x in input().split(" ")]
	moves = input()
	for i in range(n):
		if (moves[i] == "S" and l[i] == 1) or (moves[i] == "S" and l[i] == 2):
			count += 1
		elif moves[i] == "J" and l[i] > 2:
			count += 1
	print(count)