URI = "URI"
OBI = "OBI"
t = int(input())
new = []
user = input().split(" ")
for each in user:
	if len(each) == 3 and each[0] == "O" and each[1] == "B":
		new += ["OBI"]
	elif len(each) == 3 and each[0] == "U" and each[1] == "R":
		new += ["URI"]
	else:
		new += [each]
print(" ".join(new))