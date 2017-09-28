def make_combs(vet, n):
	result = []
	for i in range(n, len(vet)):
		result.append(int((vet[i]-vet[i-n])/n))
	return [min(result), max(result)]



n, i = map(int, input().split(" "))
t = 1

while(n + i != 0):
	s = 0
	temps = [0]
	for k in range(n):
		s += int(input())
		temps.append(s)
	print("Teste", t)
	temps = make_combs(temps, i)
	print(temps[0], temps[1])
	print("")
	n, i = map(int, input().split(" "))
	t+=1