t = int(input())
for _ in range(t):
    pilha = [x for x in input()]
    op = cl = count = 0
    error = False
    while(len(pilha) != 0):
        actual = pilha[-1]
        pilha.pop(-1)
        if actual == ">":
            op += 1
        elif actual == "<":
            cl += 1
        count = op - cl
        if count < 0:
            op = 0
            cl = 0

    print(min(op, cl))


"""
while(True):
    try:
        pilha = [x for x in input()]
        count = 0
        error = False
        while(len(pilha) != 0):
            actual = pilha[-1]
            pilha.pop(-1)
            if actual == ")":
                count += 1
            elif actual == "(":
                count -= 1
            if count < 0:
                error = True
                break
        if count == 0:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break
        """