import operator

alfa = dict()
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alfabeto:
    alfa[letter] = 0
n = int(input())

for l in range(0, n):
     line = input()
     line = line.upper()
     for letter in line :
         if(letter in alfabeto):
             alfa[letter] = alfa[letter] + 1
values = set(alfa.values())
values = list(values)
keys = list(alfa.keys())
values = sorted(values, reverse = True)
lis = list()
for v in values:
    lis.clear()
    for k in keys:
        if (alfa[k] == v):
            lis.append(k)
    lis.sort()
    for i in lis:
        print(i + " " + str(alfa[i]))
        
