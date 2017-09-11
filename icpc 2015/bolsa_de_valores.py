n, c = map(int, input().split(" "))
valores = []
n, c = map(int, input().split(" "))
valores = [int(x) for x in input().split(" ")]
comprar = sorted([x+c for x in valores])
vender = sorted(valores, reverse=True)

