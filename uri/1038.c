#include <stdio.h>

int main(){
	float valores[5] = {4.00, 4.50, 5.00, 2.00, 1.50};
	int num, qtd;
	scanf("%d %d", &num, &qtd);
	printf("Total: R$ %.2f\n", qtd*valores[num-1]);
	return 0;
}