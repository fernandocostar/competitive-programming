p = 0
c = int(input())
if c <= 10:
		p = 7
elif c >= 11 and c <= 30:
	p = (c-10)*1 + 7
elif c >= 31 and c <= 100:
	p = (c - 30)*2 + 27
elif c >= 101:
	p = (c - 100)*5 + 167;
print(p)
