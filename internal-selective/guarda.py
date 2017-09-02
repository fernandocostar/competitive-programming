import math as mt

user = [int(x) for x in input().split(" ")]
d = user[0]
vf = user[1]
vg = user[2]
g = rf = rg = 0
if vf >= vg:
    print("N")
else:
    g = mt.sqrt(12**2 + d**2)
    print("S") if g/vg <= 12/vf else print("N")