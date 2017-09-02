times = int(input())
user = ""
dict = {}
for i in range(times):
	user = input()
	for each in user:
		if each != " ":
			each = each.lower()
			if each in dict.keys():
				dict[each] += 1
			else:
				dict[each] = 1
	lista = 
	dict = sorted(dict, key=dict.get, reverse=True)
	print(dict)	
