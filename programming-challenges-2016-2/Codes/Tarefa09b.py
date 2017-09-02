def estaDentro(vetor, objeto):
	count = 0
	for each in vetor:
		for eachin in each:
			if eachin == objeto:
				return count
		count += 1
	return False

def checarGrupos(txt):
	vetorzaum = []
	aux = []
	flag = False
	for i in range(len(txt)):
		if txt[i][2] == '0':
			aux = [txt[i][0]]
		else:
			for k in range(4, len(txt[i]), 2):
				var = estaDentro(vetorzaum, int(txt[i][k]))
				if var:
					vetorzaum[var] += [txt[i][0]]
				else:
					aux += [txt[i][0]]
					flag = True
			if flag:
				vetorzaum += [aux]
		

			