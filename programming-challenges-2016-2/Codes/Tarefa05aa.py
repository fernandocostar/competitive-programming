import string
import operator

user = int(input())
text = ""

def countChar(s):
	d = dict.fromkeys(string.ascii_uppercase, 0)
	l = []
	for each in s:
		if each.upper() in d:
			d[each.upper()] += 1
	
	for each in d:
		l += [[d[each], each]]

	l.sort(reverse = True)

	for k in range(len(l)):
		print(l[k][1], l[k][0])

for i in range(user):
	text += input()

countChar(text)
