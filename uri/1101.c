#include <stdio.h>
int min(int a, int b){
	int r1 = a, r2 = b;
	if(r1 > r2)
		return r2;
	return r1;
}	

int max(int a, int b){
	int r1 = a, r2 = b;
	if(r1 > r2)
		return r1;
	return r2;
}	

int main(){
	int a, b, i, ma, mi, sum = 0;

	scanf("%d %d", &a, &b);
	mi = min(a, b);
	ma = max(a, b);

	
	while(a > 0 && b > 0){
		for(i = mi; i <= ma; i++){
			printf("%d ", i);
			sum += i;	
		}
		printf("Sum=%d\n", sum);
		scanf("%d %d", &a, &b);
		mi = min(a, b);
		ma = max(a,b);
		sum = 0;
	}
	
	return 0;
}