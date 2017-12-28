def b(string):
	print(int(string, 2), "dec")
	print(hex(int(string, 2))[2:], "hex")

def h(string):
	print(int(string, 16), "dec")
	print(bin(int(string, 16))[2:], "bin")

def d(string):
	print(hex(int(string))[2:], "hex")
	print(bin(int(string))[2:], "bin")

n = int(input())
for i in range(n):
	print("Case {}:".format(i+1))
	line = input().split(" ")
	if line[1] == "bin":
		b(str(line[0]))
	if line[1] == "hex":
		h(str(line[0]))
	if line[1] == "dec":
		d(str(line[0]))
	print("")
