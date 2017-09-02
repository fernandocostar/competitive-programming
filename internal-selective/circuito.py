user = [int(x) for x in input().split(" ")]

def achaMaiores(dict, num):
    total = 0
    for each in dict.keys():
        if each >= num:
            total += dict[each]
    return total

while(user[0] != 0 or user[1] != 0 or user[2] != 0):
    x = user[0]
    y = user[1]
    palitos = user[2]

    matriz = []
    encontrados = {}
    ok = 0

    for m in range(y):
        matriz += [input().split(" ")]
    for m in range(x):
        for n in range(y):
            if matriz[n][m] == "1" and ok == 0:
                ok = 1
            elif matriz[n][m] == "1" and ok != 0:
                ok += 1
            else:
                if ok not in encontrados.keys():
                    encontrados[ok] = 1
                else:
                    encontrados[ok] += 1
                ok = 0
            if n == y-1 and ok > 0:
                if ok not in encontrados.keys():
                    encontrados[ok] = 1
                else:
                    encontrados[ok] += 1
                ok = 0
    print(achaMaiores(encontrados, palitos))
    user = [int(x) for x in input().split(" ")]