#include <bits/stdc++.h>

using namespace std;

int cycles(int n){
	int count = 1;
	while(n != 1){
		if(n & 1)
			n = 3*n + 1;
		else n = n/2;
		count++;
	}
	return count;
}

int main(){
	int i, j, aux, m;
	while(scanf("%d %d", &i, &j) != EOF){
		m = 0;
		for(int k = min(i,j); k <= max(i,j); k++){
			aux = cycles(k);
			if(aux > m) m = aux;
		}
		printf("%d %d %d\n", i, j, m);
	}
	return 0;
}