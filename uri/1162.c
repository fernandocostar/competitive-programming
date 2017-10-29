#include <stdio.h>
#include <stdlib.h>

int count_sort(int* vet, int tam){
	int i, j, aux, count = 0;
	for(i = 0; i < tam; i++){
		for(j = i+1; j < tam; j++){
			if(vet[i]>vet[j]){
				count++;
				aux = vet[i];
				vet[i] = vet[j];
				vet[j] = aux;
			}
		}
	}
	return count;
}

int main(){
	int i, j, n, k, p;
	int vet[50];
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf("%d", &k);
		for(j = 0; j < k; j++){
			scanf("%d", &vet[j]);
		}
		p = count_sort(vet, k);
        printf("Optimal train swapping takes %d swaps.\n", p);
	}

	return 0;
}