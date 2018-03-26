#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, aux, y = 0, n = 0;
	cin >> t;
	for(int i = 0; i < t; i++){
		cin >> aux;
		if(!aux) y++;
		else n++;
	}
	if(y > n) printf("Y\n");
	else printf("N\n");
	return 0;
}