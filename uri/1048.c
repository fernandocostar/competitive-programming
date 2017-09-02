#include <stdio.h>

int main(){
	float in;
	scanf("%f", &in);

	if(in <= 400){
		printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", in + in*0.15, in*0.15, 15);
	}else if(in <= 800){
		printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", in + in*0.12, in*0.12, 12);
	}else if(in <= 1200){
		printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", in + in*0.10, in*0.10, 10);
	}else if(in <= 2000){
		printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", in + in*0.07, in*0.07, 7);
	}else{
		printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", in + in*0.04, in*0.04, 4);
	}

	return 0;
}