#include <bits/stdc++.h>

using namespace std;

struct integer{
    int info;
    int mod;
    bool operator<(integer b)const {
        if(info % mod != b.info % mod) return (info % mod) < (b.info % mod);
        else if(abs((info + b.info) % 2) == 1){
            return info % 2;
        }
        if(info % 2) return info > b.info;
        return info < b.info;
    }
};

int main(){
    int n, m, aux;
    scanf("%d %d", &n, &m);
    printf("%d %d\n", n, m);
    while(n+m) {
        vector<integer> v;
        for (int i = 0; i < n; i++) {
            scanf("%d", &aux);
            integer in;
            in.info = aux;
            in.mod = m;
            v.push_back(in);
        }
        sort(v.begin(), v.end());
        for (int i = 0; i < n; i++) {
            printf("%d\n", v.at(i).info);
        }
        scanf("%d %d", &n, &m);
        printf("%d %d\n", n, m);
    }
    return 0;
}