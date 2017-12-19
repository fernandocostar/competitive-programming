line1 = [int(x) for x in input().split(" ")]
line2 = [int(x) for x in input().split(" ")]
result = 0
total = [i for i in range(5) if line1[i] + line2[i] == 1]
print("N") if len(total) != 5 else print("Y")