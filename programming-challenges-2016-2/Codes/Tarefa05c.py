import itertools

def fazerAnagramas(x):
    vet = ["".join(perm) for perm in itertools.permutations(x)]
    return vet
def ordenar(x):
    temp = []
    x = sorted(x)
    actual = 0
    for i in range(len(x[0])):




user = int(input())
vet = []
for i in range(user):
    vet += [input()]
aux = []
result = []
for each in vet:
    aux += [fazerAnagramas(each)]
for each in aux:
    result += [sorted(each, key=lambda L: (L.lower(), L))]
for each in result:
    for opa in each:
        print(opa)