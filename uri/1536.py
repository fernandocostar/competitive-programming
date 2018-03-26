n = int(input())
for i in range(n):
	a = b = 0
	p1 = input().split(" ")
	p2 = input().split(" ")
	a += int(p1[0]) + int(p2[2])
	b += int(p1[2]) + int(p2[0])
	if a != b:
		print("Time 1") if a > b else print("Time 2")
	elif int(p1[2]) > int(p2[2]) or int(p1[2]) < int(p2[2]):
		print("Time 1") if int(p1[2]) < int(p2[2]) else print("Time 2")
	else:
		print("Penaltis")