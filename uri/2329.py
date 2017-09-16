def check_max(x, n, k):
	r = 0
	for i in range(k):
		r += tams[i]//x
		if r >= n:
			return True
	return False

def bs(x, n, k):
	r = 0
	start = 1
	end = x
	while(start <= end):
		middle = (start + end)//2
		if check_max(middle, n, k):
			r = max(middle, r)
			start = middle+1
		else:
			end = middle - 1
	return r

n = int(input())
k = int(input())
tams = [0]*10001
inp = [int(x) for x in input().split(" ")]
m = max(inp)
for i in range(k):
	tams[i] = inp[i]
r = bs(m, n, k)
print(r)