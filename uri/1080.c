#include <stdio.h>

int main(){
	int i, aux, biggest = -1, index;

	for(i = 1; i <= 100; i++){
		scanf("%d", &aux);
		if(aux > biggest){
			biggest = aux;
			index = i;
		}
	}

	printf("%d\n%d\n",biggest, index);

	return 0;
}