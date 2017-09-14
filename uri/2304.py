i, n = map(int, input().split(" "))
jogadores = {"D":i, "E":i, "F":i}
for _ in range(n):
	user = [x for x in input().split(" ")]
	if user[0] == "C":
		jogadores[user[1]] -= int(user[2])
	elif user[0] == "V":
		jogadores[user[1]] += int(user[2])
	elif user[0] == "A":
		jogadores[user[1]] += int(user[3])
		jogadores[user[2]] -= int(user[3])
result = [str(jogadores[x]) for x in sorted(jogadores)]
print(" ".join(result))
