
def main():

    t = int(input())
    z = 1
    while(t):
        p, n = input().split()
        p = int(p)
        n = int(n)
        autoresEscolhidos = []
        for i in range(n):
            autoresEscolhidos.append(input())
        publicacoes = []
        for j in range(p):
            public = input().split(":")[0]
            pub = public.split(", ")
            newPub = []
            for i in range(0, len(pub), 2):
                newPub.append(pub[i] + ", " + pub[i + 1])
            publicacoes.append(newPub)
        pubUm = []
        aux = 0
        for p in publicacoes:
            for i in p:
                if(i == "Erdos, P."):
                    for j in p:
                        if(j != "Erdos, P."):
                            pubUm.append(j)
                    aux = 1
                    break
            if(aux):
                pos = publicacoes.index(p)
                publicacoes[pos] = -1
                aux = 0
        pubsFinal = []
        pubsFinal.append(pubUm)
        pubAtual = pubUm
        aux2 = 0
        while(publicacoes):
            for p in publicacoes:
                if(p != -1):
                    aux2 = 1
                    break
            if(aux2):
                nextPub =[]
                for p in publicacoes:
                    if(p != -1):
                        x = 0
                        for i in p:
                            if i in pubAtual:
                                x = 1
                            if(x):
                                for u in p:
                                    if(u not in pubAtual):
                                        nextPub.append(u)
                            break
                pubsFinal.append(nextPub)
            else:
                break
            for i in publicacoes:
                if(i != -1):
                    publicacoes[publicacoes.index(i)] = -1
                    break
            aux2 = 0
            pubAtual = nextPub
        valoresEquivalentes = []
        for i in range(len(autoresEscolhidos)):
            valoresEquivalentes.append("00")

        atual = 1
        for pf in pubsFinal:
            for i in pf:
                if(i in autoresEscolhidos):
                    valoresEquivalentes[autoresEscolhidos.index(i)] = atual
            atual +=1
        print('Teste #' + str(z))
        for i in range(len(autoresEscolhidos)):
            print(autoresEscolhidos[i] + " " + str(valoresEquivalentes[i]))
        z +=1
        t-=1


main()
