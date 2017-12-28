line = [int(x) for x in input().split(" ")]
while(line[0] != 0):
	res = int(line[0]*((line[2]*line[1])/(line[2]-line[0])))
	print(res,"paginas") if res != 1 else print(res,"pagina")
	line = [int(x) for x in input().split(" ")]
