#include <bits/stdc++.h>

using namespace std;

#define mp make_pair

void DFSutil(set<int> g[], int s, int visited[], set<int> *l){
    visited[s]++;
    (*l).insert(s+97);
    set<int>::iterator it;
    for(it = g[s].begin(); it != g[s].end(); ++it){
        if(!visited[*it]){
            DFSutil(g, *it, visited, l);
        }
    }
    return;
}

void printSet(set<int> s){
    set<int>::iterator it;
    for(it = s.begin(); it != s.end(); ++it){
        printf("%c,", *it);
    }
    printf("\n");
    return;
}

int main(){
    int n, nodes, edges;
    char u, v;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        printf("Case #%d:\n", i);
        scanf("%d %d", &nodes, &edges);
        set<int> g[nodes];
        for(int j = 0; j < edges; j++){
            scanf(" %c %c", &u, &v);
            if(u > v)swap(u,v);
            g[u-97].insert(v-97);
            g[v-97].insert(u-97);
        }
        int visited[nodes];
        memset(visited, 0, nodes*sizeof(int));
        int total = 0;
        set<int> line;
        for(int j = 0; j < nodes; j++){
            if(!visited[j]){
                DFSutil(g, j, visited, &line);
                total++;
            }else{
                continue;
            }
            printSet(line);
            line.clear();
        }
        printf("%d connected components\n\n",total);

    }
    return 0;
}