#include <stdio.h>
#include <stdlib.h>

typedef struct matriz {
	int **grafo;
	int tam;
} MDA;

MDA cria(int tam) {
	MDA *resp = (MDA *)malloc(sizeof(MDA));

	resp->grafo = (int **)malloc(sizeof(int*)*tam);
	resp->tam = tam;
	int i;
	for(i = 0; i < tam; i++) {
		resp->grafo[i] = (int *) malloc(sizeof(int)*tam);
	}
	zera(resp);
	return resp;
}

void zera(MDA *m) {
	int i, j;
	for(i = 0; i < m->tam; i++) {
		for(j = 0; j < m->tam; j++) {
			m-grafo[i][j] = 0;
		}
	}
}

void insere(MDA *m, int i, int j) {
	m->grafo[i-1][j-1] = 1;
}

void libera(MDA *m) {
	int i;
	for(i = 0; i < m->tam; i++) {
		free(m->grafo[i]);
	}
	free(m->grafo);
	free(m);
}

int main(void){
	int t, m, n;
	scanf("%d", &t);
	int i;
	for(i = 0; i < t; i++){
		scanf("%d %d", &n, &m);
		MDA* g = cria(n);
		int j;
		for(j = 0; j < m; j++){
			int v1, v2;
			scanf("%d %d", &v1, &v2);
			insere(g, v1, v2);
		} 
		int count = 0;
		int* visitados = (int*)calloc(sizeof(int)*n);
		for(j = 0; j < n; j++){
			if(visitados[j] == 0) {
				busca(visitados, g, j);
				count++;
			}
		}
		
	}

	return 0;
}