#include <stdio.h>

int main(){
	int n, i;
	char aux;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		int toggle = 1;

		scanf(" %c", &aux);
		while(aux != '\n'){
			if(aux != ' ' && toggle == 1){
				printf("%c", aux);
				toggle = 0;
			}else if(aux == ' ') toggle = 1;
			scanf("%c", &aux);
		}
		printf("\n");
	}
	return 0;
}