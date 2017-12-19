n = int(input())
while(n != 0):
    linha = input().split(" ")
    mary = len([x for x in linha if x == "0"])
    jon = len([x for x in linha if x == "1"])
    print("Mary won", mary, "times and John won", jon, "times")
    n = int(input())