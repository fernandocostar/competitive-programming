#include <bits/stdc++.h>

using namespace std;

typedef struct rena{
	string nome;
	int idade;
	int peso;
	float altura;
	bool operator<(rena outro) const{
		if(peso != outro.peso)return peso > outro.peso;
		if(idade != outro.idade)return idade < outro.idade;
		if(altura != outro.altura)return altura < outro.altura;
		return nome < outro.nome;
	}
}Rena;

int main(){
	int t, total, corte, idade, peso;
	string nome;
	float altura;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		printf("CENARIO {%d}\n", i+1);
		scanf("%d %d", &total, &corte);
		vector<Rena> v;
		for(int j = 0; j < total; j++){
			cin >> nome;
			scanf("%d %d %f", &peso, &idade, &altura);
			Rena r;
			r.nome = nome;
			r.peso = peso;
			r.idade = idade;
			r.altura = altura;
			v.push_back(r);
		}
		sort(v.begin(), v.end());
		for(int j = 0; j < corte; j++){
			printf("%d - ", j+1);
			cout << v.at(j).nome << endl;
		}
	}
	return 0;
}