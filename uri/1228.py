while True:
	try:
		n = int(input())
		l1 = [int(x) for x in input().split()]
		l2 = [int(x) for x in input().split()]
		count = 0
		for i in range(n):
			index = l1.index(l2[i])
			count += index - i
			l1.pop(index)
			l1.insert(i, l2[i])
		print(count)
	except EOFError:
		break