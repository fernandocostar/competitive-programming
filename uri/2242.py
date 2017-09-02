w = input()
v = list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], w))
print("S" if v == list(reversed(v)) else "N")