#include <stdio.h>
#include <stdlib.h>

int compare_function(const void *a,const void *b) {
int *x = (int *) a;
int *y = (int *) b;
return *x - *y;
}

int main(){

	int t, i, n, j, count = 0;

	scanf("%d", &t);

	for(i = 0; i < t; i++){
		scanf("%d", &n);
		int array[n];
		for(j = 0; j < n; j++){
			scanf("%d", &array[j]);
		}
		qsort(array, n, sizeof(int), compare_function);
		for(j = 0; j < n; j++){
			if(array[j] != array[j+1]){
				count++;
			}
		}
		printf("%d\n", count);
		count = 0;
	}

	return 0;
}