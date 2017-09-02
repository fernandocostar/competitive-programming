def retorna_fib(num):
	array = [0, 1]
	for i in range(2, num+1):
		array += [array[i-2]+array[i-1]]
		pass
	return array

user = int(input())
for _ in range(user):
	fib = int(input())
	result = retorna_fib(fib)
	print("Fib({}) = {}".format(fib, result[fib]))