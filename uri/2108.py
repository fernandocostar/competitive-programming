m = -1
b = ""
l = input()
while l != "0":
	l = l.split(" ")
	for each in l:
		if len(each) >= m:
			m = len(each)
			b = each
	s = [str(len(t)) for t in l]
	print("-".join(s))
	l = input()
print("\nThe biggest word: "+b)
