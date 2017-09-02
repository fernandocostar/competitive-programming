t = int(input())
acertos = [0, 0, 0]
totais = [0, 0, 0]
result = []
for _ in range(t):
    nome = input()
    s, b, a = map(int, input().split(" "))
    totais[0] += s
    totais[1] += b
    totais[2] += a
    s, b, a = map(int, input().split(" "))
    acertos[0] += s
    acertos[1] += b
    acertos[2] += a
for i in range(3):
    result.append(round(acertos[i]/totais[i]*100, 2))
print("Pontos de Saque: %.2f %%."%result[0])
print("Pontos de Bloqueio: %.2f %%."%result[1])
print("Pontos de Ataque: %.2f %%."%result[2])
