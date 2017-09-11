#include <stdio.h>

int main(void) {
	int certo;
	scanf(" %d", &certo);

	int resposta[5];
	scanf("%d %d %d %d %d", &resposta[0], &resposta[1], &resposta[2], &resposta[3], &resposta[4]);

	int acertaram = 0;
	int i;
	for(i = 0; i < 5; i++) {
		if(resposta[i] == certo) acertaram++;
	}

	printf("%d\n", acertaram);

	return 0;
}