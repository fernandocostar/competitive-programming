user = input().split(" ")
user = [int(x) for x in user]
dif = []
pontos = user[1]
pontosmax = 0
pontosposi = 0

def calculaPontos(vetor):
    total = 0
    for each in vetor:
        if each == 0:
            total += 1
        elif each == 1:
            total += 3
        else:
            break
    return total


for i in range(user[0]):
    entrada = input().split(" ")
    entrada = [int(x) for x in entrada]
    difa = entrada[0] - entrada[1]
    if difa > 0:
        pontosmax += 3
        pontosposi += 3
    elif difa == 0:
        pontosmax += 1
    if difa <= 0:
        dif.append(difa)
dif = sorted(dif, reverse=True)
print(dif)

for k in range(len(dif)):
    if pontos == 0:
        break
    if dif[k] == 0:
        pontos -= 1
        dif[k] += 1
    else:
        if pontos >= (-dif[k])+1:
            pontos += (dif[k]-1)
            dif[k] = 1
        elif pontos == -dif[k]:
            pontos = 0
            dif[k] = 0
            break
        else:
            break

print(calculaPontos(dif)+pontosposi)
