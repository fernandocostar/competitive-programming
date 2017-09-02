#include <stdio.h>

int get_leds(char a, int* array){
	char c = a;
	return array[(int)(c-48)];
}

int main(){
	int leds[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
	char actual;
	int i, n, sum;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		sum = 0;
		scanf(" %c", &actual);
		while(actual != '\n'){
			sum += get_leds(actual, leds);
			scanf("%c", &actual);
		}
		printf("%d leds\n", sum);
	}
	return 0;
}