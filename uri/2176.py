s = input()
count = 0
for each in s:
    if each == "1":
        count += 1
print(s+"0") if count % 2 == 0 else print(s+"1")