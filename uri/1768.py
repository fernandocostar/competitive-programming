def fazarvore(n):
	texto = ""
	for i in range(n//2):
		texto += " "
	texto += "*"
	for i in range(n//2+1):
		print(texto)
		texto = texto[1:] + "**"
	#
	texto = ""
	for i in range(n//2):
		texto += " "
	texto += "*"
	for i in range(1):
		print(texto)
		texto = texto[1:] + "**"
	print(texto)
	print("")
while True:

	try:
		n = int(input())
		if not n & 1:
			n -= 1

		fazarvore(n)
	except EOFError:
		break