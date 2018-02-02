
n = int(input())
for i in range(n):
	vet = [int(x) for x in input().split(" ")[1:]]
	media = sum(vet)/len(vet)
	soma = 0
	for each in vet:
		if each > media:
			soma += 1
	print("%.3f%%"%(round((soma/len(vet))*100000)/1000))