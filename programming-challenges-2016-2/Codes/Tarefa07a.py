from fractions import Fraction
times = []
probs = []
quarta = []
semi = []
final = []

for i in range(16):
	times += [input()]

for k in range(16):
	probs += [input().split(" ")]

for f in range(len(probs)):
	for y in range(len(probs[f])):
		probs[f][y] = float(probs[f][y])


for m in range(16):
    if m % 2 == 0:
        quarta += [probs[m][m+1]]
    else:
        quarta += [probs[m][m-1]]

for g in range(0, 16, 2):
    if (g % 4 == 0):
        semi += [(((probs[g][g + 2] / quarta[g + 2]) * quarta[g]) + ((probs[g][g + 3] / quarta[g + 3]) * quarta[g]))]
        semi += [(((probs[g+1][g + 2] / quarta[g + 2]) * quarta[g+1]) + ((probs[g+1][ g + 3] / quarta[g + 3]) * quarta[g+1]))]
    else:
        semi += [(((probs[g][ g - 2] / quarta[g - 2]) * quarta[g]) + ((probs[g][g - 1] / quarta[g - 1]) * quarta[g]))]
        semi += [(((probs[g + 1][ g - 2] / quarta[g - 2]) * quarta[g + 1]) + ((probs[g + 1][g - 1] / quarta[g -1]) * quarta[g + 1]))]
                 
for g in range(0, 16, 4):
    if(g % 8 == 0):
    	for k in range(4):
        	final += [(((probs[g+k][g + 4] / semi[g + 4])*semi[g+k]) + ((probs[g+k][g + 5]/semi[g + 5])*semi[g+k]) + ((probs[g+k][g + 6]/semi[g + 6])*semi[g+k]) + ((probs[g+k][g + 7]/semi[g + 7])*semi[g+k]))]
    else:
    	for k in range(4):
    		final += [((probs[g+k][g -1] / semi[g -1])*semi[g+k])+((probs[g+k][g -2]/semi[g -2])*semi[g+k]) + ((probs[g+k][g -3]/semi[g -3])*semi[g+k]) + ((probs[g+k][g -4]/semi[g -4])*semi[g+k])]
       
CAMPEAOCARALHO = []


for g in range(0, 16, 8):
	if g == 0:
		for m in range(8):
			CAMPEAOCARALHO += [((probs[g +m][g+8]/final[g+8])*final[g+m]) + ((probs[g+m][g+9]/final[g+9])*final[g+m]) + ((probs[g+m][g+10]/final[g+10])*final[g+m]) + ((probs[g+m][g+11]/final[g+11])*final[g+m]) + ((probs[g+m][g+12]/final[g+12])*final[g+m]) + ((probs[g+m][g+13]/final[g+13])*final[g+m]) + ((probs[g+m][g+14]/final[g+14])*final[g+m]) + ((probs[g+m][g+15]/final[g+15])*final[g+m])]		
	else:
		for m in range(8):
			CAMPEAOCARALHO += [((probs[g +m][g-1]/final[g-1])*final[g+m] + (probs[g+m][g-2]/final[g-2])*final[g+m] + (probs[g+m][g-3]/final[g-3])*final[g+m] + (probs[g+m][g-4]/final[g-4])*final[g+m] + (probs[g+m][g-5]/final[g-5])*final[g+m] + (probs[g+m][g-6]/final[g-6])*final[g+m] + (probs[g+m][g-7]/final[g-7])*final[g+m] + (probs[g+m][g-8]/final[g-8])*final[g+m])]		

maior = 0
for each in times:
    if len(each) > maior:
        maior = len(each)

espacos = []

for i in range(len(times)):
    espacos += [maior - len(times[i])]

espaco = ""

for i in range(16):
    for k in range(espacos[i]):
        espaco += " "

    proba = CAMPEAOCARALHO[i]/100

    print(times[i]+espaco+" "+"%.2f"%proba+"%")
    espaco = ""







