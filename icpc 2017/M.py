a1 = int(input())
a2 = int(input())
a3 = int(input())
tempos = []

"""se a maquina for posicionada no andar superior"""
tempos.append(a2*2 + a3*4)
"""se a maquina for posicionada no andar do meio"""
tempos.append(a1*2 + a3*2)
"""se a maquina for posicionada no andar de baixo"""
tempos.append(a1*4 + a2*2)
print(min(tempos))