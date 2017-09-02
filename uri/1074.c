#include <stdio.h>

int main(){

	int n, i, aux;

	scanf("%d", &n);

	for(i = 0; i < n; i++){
		scanf("%d", &aux);
		if(aux % 2 == 0){
			if(aux < 0){
				printf("EVEN NEGATIVE\n");
			}else if(aux > 0){
				printf("EVEN POSITIVE\n");
			}else{
				printf("NULL\n");
			}
		}else{
			if(aux < 0){
				printf("ODD NEGATIVE\n");
			}else if(aux > 0){
				printf("ODD POSITIVE\n");
			}
		}
	}

	return 0;
}