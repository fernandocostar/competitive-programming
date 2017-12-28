#include <bits/stdc++.h>

using namespace std;

int main(){
	vector<int> pedidos, refeicoes;
	int aux;
	for(int i = 0; i < 3; i++){
		scanf("%d", &aux);
		refeicoes.push_back(aux);
	}
	for(int i = 0; i < 3; i++){
		scanf("%d", &aux);
		pedidos.push_back(aux);
	}
	aux = 0;
	for(int i = 0; i < 3; i++){
		if(refeicoes.at(i)-pedidos.at(i) < 0)aux += -(refeicoes.at(i)-pedidos.at(i));
	}
	printf("%d\n", aux);
	return 0;
}