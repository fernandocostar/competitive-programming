while(True):
    try:
        user = input()
        rev = user[::-1]
        palin = False
        espe = False
        if user == rev:
            palin = True
        dict = {"A": "A", "E": "3", "H": "H", "I": "I", "J": "L", "L": "J", "M": "M", "O": "O", "S": "2", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "5", "1": "1", "2": "S", "3": "E", "5": "Z","8":"8", "0":"0"}

        aux = 0

        for k in range(len(user)//2):
            if dict.get(user[k]) != -1:
                if dict.get(user[k]) == rev[k]:
                    aux += 1
        if aux == len(user)//2:
            espe = True

        if palin and espe:
            print(user, "- palindromo espelhada")
        elif palin and not espe:
            print(user, "- palindromo regular")
        elif espe and not palin:
            print(user, "- espelhada regular")
        else:
            print(user, "- regular")
    except EOFError:
        break
