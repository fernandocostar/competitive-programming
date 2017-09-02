def girarHorizontal(x):
    temp = ""
    temp += x[0]+x[2]+x[4]+x[1]+x[3]+x[5]
    x = temp
    return x

def girarVertical(x):
    temp = ""
    temp += x[4]+x[0]+x[2]+x[3]+x[5]+x[1]
    x = temp
    return x

def cuboIgual(x, y):
    for m in range(4):
        for n in range(4):
            y = girarHorizontal(y)
            if x == y:
                return True
            y = girarHorizontal(y)
        y = girarVertical(y)
    return False

while(True):
    try:
        cube = input()
        cubo1 = cube[:6]
        cubo2 = cube[6:12]
        resultado = cuboIgual(cubo1, cubo2)
        if resultado:
            print("V")
        else:
            print("F")
    except EOFError:
        break