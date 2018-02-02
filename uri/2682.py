ant = at = -1
while True:
    try:
        ant = at
        at = int(input())
        if at <= ant:
            print(ant + 1)
            break
    except EOFError:
        break