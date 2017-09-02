def lerTudo():
    temp = ""
    user = input()
    while(user != "#"):
        temp += " " + user
        user = input()
    return temp
user = lerTudo()[:]
vetor = user.split(" ")
vetaux = []
result = []
vetor.pop(0)
lenVet = len(vetor)
for each in vetor:
    vetaux += ["".join(sorted(each.upper()))]
for i in range(lenVet-1):
    aux = False
    if vetaux[i] != "falsso":
        for k in range(i+1, lenVet):
            if vetaux[i] == vetaux[k]:
                vetaux[k] = "falsso"
                aux = True
        if aux:
            vetaux[i] = "falsso"
for k in range (len(vetor)):
    if vetaux[k] != "falsso":
        result += [vetor[k]]
result = sorted(result, key=lambda s: s.lower())
for each in result:
    print(each)

