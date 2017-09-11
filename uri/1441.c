#include <stdio.h>

int h(int num){
	int calc;
	if(num == 1) return 1;
	if(num % 2 == 0){
		calc = h(num/2);
		if(calc > num) return calc;
		return num;
	}else{
		calc = h(3 * num + 1);
		if(calc > num) return calc;
		return num;
	}
}

int main(){
	int n, r;
	scanf("%d", &n);
	while(n != 0){
		r = h(n);
		printf("%d\n", r);
		scanf("%d", &n);
	}
	return 0;
}