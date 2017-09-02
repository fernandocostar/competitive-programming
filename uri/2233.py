i1 = input()
i2 = input()
i3 = input()
i1 = int(i1, 16)
i2 = int(i2, 16)
i3 = int(i3, 16)
result = 0
result += (i1**2)//(i2**2)
print(result)
result += result * ((i2**2)//(i3**2))
print(result)
result += 1
print(result)
print ("%02x"%result)