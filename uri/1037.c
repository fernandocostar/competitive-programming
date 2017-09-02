#include <stdio.h>

int main(){
	float in;
	scanf("%f", &in);

	if(in >= 0 && in <=25){
		printf("Intervalo [0,25]\n");
	}else if(in > 25 && in <= 50){
		printf("Intervalo (25,50]\n");
	}else if(in > 50 && in <= 75){
		printf("Intervalo (50,75]\n");
	}else if(in > 75 && in <= 100){
		printf("Intervalo (75,100]\n");
	}else{
		printf("Fora de intervalo\n");	
	}

	return 0;
}

