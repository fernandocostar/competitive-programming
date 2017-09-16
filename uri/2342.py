m = int(input())
r = 0
entrada = [x for x in input().split(" ")]
r = (int(entrada[0])*int(entrada[2]) if entrada[1] == "*" else int(entrada[0])+int(entrada[2]))
print("OK") if r <= m else print("OVERFLOW") 