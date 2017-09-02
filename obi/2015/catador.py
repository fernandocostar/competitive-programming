n, m = map(int, input().split(" "))
conchas = [int(x) for x in input().split(" ")]
indices = [int(x) for x in input().split(" ")]
indices = sorted(indices)
c = 0
for i in range(len(indices)):
    indice = indices[i]-1
    length = len(conchas)
    c = conchas[indice]
    for k in range(indice - c, indice + c + 1):
        if k >= 0 and k < length and conchas[k] > 0:
            conchas[k] -= 1
print(sum(conchas))
