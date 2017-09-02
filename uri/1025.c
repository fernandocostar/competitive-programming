#include <stdio.h>
#include <stdlib.h>

int is_in(int num, int tam, int* array){
	int j;
	for(j = 0; j < tam; j++){
		if(array[j] == num) return j;
	}
	return -1;
}

int main(){
	int a, b, i, pos, num, count = 1;

	scanf("%d %d", &a, &b);
	while(a + b != 0){
		printf("CASE# %d\n",count);
		int* marmores = (int*) malloc(a*sizeof(int));
		int* testes = (int*) malloc(a*sizeof(int));
		for(i = 0; i < a; i++){
			scanf("%d", &marmores[i]);
		}
		for(i = 0; i < b; i++){
			scanf("%d", &testes[i]);
		}

		for(i = 0; i < b; i++){
			pos = is_in(testes[i], a, marmores);
			if(pos != -1){
				num = testes[i];
				pos += 2;
				printf("%d found at %d\n", num, pos);
			}
		}

		if(pos == -1){
			printf("%d not found\n", num);
		}

		free(marmores);
		free(testes);


		scanf("%d %d", &a, &b);
		count++;
	}

	return 0;
}