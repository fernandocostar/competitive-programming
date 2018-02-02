#include <bits/stdc++.h>

using namespace std;

typedef struct pedido{
    string nome;
    char tam;
    string cor;
}Pedido;

bool compare(Pedido a, Pedido b){
    if(a.cor != b.cor)return a.cor < b.cor;
    if(a.tam != b.tam) return a.tam > b.tam;
    return a.nome < b.nome;
}

Pedido arr[61];

int main(){
    int n;
    string nome, cor;
    char tam;
    scanf("%d", &n);
    while(n) {
        cin.ignore();
        for (int i = 0; i < n; i++) {
            getline(cin, arr[i].nome);
            cin >> arr[i].cor >> arr[i].tam;
            cin.ignore();
        }
        sort(arr, arr+n, compare);
        for(int i = 0; i < n; i++){
            cor = arr[i].cor;
            tam = arr[i].tam;
            nome = arr[i].nome;
            cout << cor << " " << tam << " " << nome << endl;
        }
        scanf("%d", &n);
        if(n)cout << endl;
    }
    return 0;
}