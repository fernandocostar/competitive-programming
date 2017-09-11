#include <stdio.h>
#include <stdlib.h>

void sort(int* array, int tam){
	int i, j, aux;
	for(i = 0; i < tam-1; i++){
		for(j = 0; j < tam-1; j++){
			if(array[i] > array[i+1]){
				aux = array[i+1];
				array[i+1] = array[i];
				array[i] = aux;
			}
		}
	}
}

void solve(int* valores){

}

int main(){
	int n, c, k;
	int i, j, d;
	scanf("%d %d %d", &n, &c, &k);
	int numeros[10] = {0};
	for(i = 0; i < n; i++){
		for(j = 0; j < c; j++){
			scanf("%d", &d);
			numeros[d]++;
		}
	}
	return 0;
}