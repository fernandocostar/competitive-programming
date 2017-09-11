fatoriais = []
start = 1
count = 1
while(start <= 1000000):
	fatoriais.append(start)
	start *= count
	count += 1
result = 0
user = int(input())
k = user
for each in reversed(fatoriais):
	result += k//each
	k = k % each
	if k == 0:
		break
print(result)