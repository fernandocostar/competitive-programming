#include <stdio.h>

long int fatorial(int num){
	if(num < 2){
		return 1;
	}
	return num * fatorial(num-1);	
}

int main(){
	int i;
	long int j;

	scanf("%d", &i);

	j = fatorial(i);

	printf("%ld\n", j);

	return 0;
}