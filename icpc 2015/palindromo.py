user = input()

def get_all_substrings(input_string):
  length = len(input_string)
  return [len(input_string[i:j+1]) for i in range(length) for j in range(i,length)]

def maior_palindromo(vetor):
	todos = []
	if vetor == reversed(vetor):
		return len(vetor)
	else:
		todos = get_all_substrings(str(vetor))
		print(todos)
	return max(todos)


new = []
especiais = [int(x) for x in input().split(" ")]

if(especiais[0] == 0 and len(especiais) == 1):
	new = [x for x in user]
else:	
	new = [user[x-1] for x in especiais]

print(maior_palindromo(new))
