#include <stdio.h>
#include <stdlib.h>

long int fib(int n, int* c){
	if(n < 2){
		c++;
		return n;
	}else{
		*c += 2;
		return fib(n-1, c) + fib(n-2, c);	
	}
}

int main(){
	int t, i, num, calls = 0, result;
	scanf("%d", &t);
	for(i = 0; i < t; i++){
		scanf("%d", &num);
		result = fib(num, &calls);
		printf("fib(%d) = %d calls = %d\n",num,calls, result);
		calls = 0;
	}
	return 0;
}