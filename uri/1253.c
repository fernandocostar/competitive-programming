#include <stdio.h>

char solve(char c, int shift){
	int s = shift % 26;
	if((c - s) < 65){
		return (c - s) + 26;
	}
	return (c - s);
}

int main(){
	int i, n, shift, cont = 0;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		char actual;
		char palavra[50] = {0};
		scanf(" %[^\n]", palavra); 
		scanf("%d", &shift);
		cont = 0;
		actual = palavra[cont];
		while(actual != 0 && cont < 50){
			printf("%c", solve(actual, shift));
			cont++;
			actual = palavra[cont];
		}
		printf("\n");
	}

	return 0;
}