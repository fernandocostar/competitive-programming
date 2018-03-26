n = int(input())
while(n):
	k = h = 1
	d = len(str(2**((n-1)*2)))
	ei = "".join(" " for i in range(d-1))
	for i in range(n):
		k = h
		print("".join([" " for k in range(d- len(str(2**i)))]), end="")
		for j in range(n):
			if(j != n-1):
				print(k, end="".join([" " for k in range(d - len(str(2**(i+j+1))) +1)]))
			else:
				print(k, end="")
			k *= 2
			m = k//2
		print("")
		h *= 2
	n = int(input())
	if(n):
		print("")
print("")