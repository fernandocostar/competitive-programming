n = int(input())
factorials = []
actual = 1
i = 1
while(actual < n):
    actual *= i
    factorials.append(actual)
    i += 1
count = 0
for each in reversed(factorials):
    calc = n//each
    if calc >= 1:
        count += calc
    n = n % each
print(count)