n = int(input())
l = [int(x) for x in input().split(" ")]
flag = True
for i in range(1, len(l)):
	if l[i] < l[i-1]:
		print(i+1)
		flag = False
		break
if flag:
	print(0)