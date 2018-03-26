t = int(input())
for i in range(t):
	c = int(input())
	insts = []
	p = 0
	for j in range(c):
		op = input()
		if op == "LEFT":
			p -= 1
		elif op == "RIGHT":
			p += 1
		else:
			op = insts[int(op.split(" ")[2])-1]
			if op == "LEFT":
				p -= 1
			elif op == "RIGHT":
				p += 1
		insts.append(op)
	print(p)
