//READING STRING PROBLEM :(
#include <stdio.h>
#include <iostream>

using namespace std;

int resolve(char *frase, int j){
	int i = 0, soma = 0;
	while(frase[i] != '\0'){
		soma += j + (frase[i]-65) + i;
		i++;
	}
	return soma;
}

int main(){
	char atual[51];
	int i, j, n, tam, count;
	cin >> n;
	for(i = 0; i < n; i++){
		count = 0;
		cin >> tam;
		cout << tam << endl;
		for(j = 0; j < tam; j++){
			cin.getline(atual, 51);
			count += resolve(atual, j);
		}
		cout << count << endl;
	}
	return 0;
}