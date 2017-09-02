user = int(input())

def retorna_fib(num):
	array = [0, 1]
	for i in range(2, num):
		array += [array[i-2]+array[i-1]]
	return array
array = retorna_fib(user)	
print(*array)