while True:
	try:
		n = int(input())
		s = ["3" for i in range(n)]

		for i in range(n):
			if i == n//2 and n%2:
				s[n//2] = "2"
				print("".join(s))
				s[n//2] = "3"
			else:
				s[i] = "1"
				s[-i-1] = "2"
				print("".join(s))
				s[i] = "3"
				s[-i-1] = "3"
	except EOFError:
		break