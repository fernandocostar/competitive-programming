a, b = map(int, input().split(" "))
m = {}
for i in range(a):
	p, v = input().split(" ")
	m[p] = int(v)
for i in range(b):
	linha = input()
	texto = ""
	while(linha != "."):
		texto += " " + linha
		linha = input()
	t = 0
	for each in texto.split(" "):
		if each in m.keys():
			t += m[each]
	print(t)