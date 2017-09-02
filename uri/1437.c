#include <stdio.h>

int main(){
	int t, i, status;
	char c;
	scanf("%d", &t);
	while(t != 0){
		status = 0;
		for(i = 0; i < t; i++){
			scanf(" %c", &c);
			if(c == 'D') status++;
			if(c == 'E') status--;
		}

		if(status % 4 == 0) printf("N\n");
		else if((status < 0 && status % 4 == -1) || (status > 0 && status % 4 == 3)) printf("O\n");
		else if((status > 0 && status % 4 == 1) || (status < 0 && status % 4 == -3)) printf("L\n");
		else printf("S\n");

		scanf("%d", &t);
	}


	return 0;
}