#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

int main(){
    int n, max_length;
    string aux;
    cin >> n;
    while(n){
        max_length = 0;
        vector<string> nomes;
        for(int i = 0; i < n; i++){
            cin >> aux;
            nomes.push_back(aux);
            if(aux.size() > max_length) max_length = aux.size();
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < max_length - nomes.at(i).size(); j++) cout << " ";
            cout << nomes.at(i) << endl;
        }
        cin >> n;
	if(n) cout << endl;
    }
    return 0;
}
