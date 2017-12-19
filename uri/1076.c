#include <stdio.h>
#include <stdlib.h>

#define MAX_P 100
#define MAX 100

typedef struct pilha {
	int topo;
	int vetor[MAX_P];
} Pilha;

Pilha criaPilha() {
	Pilha p;
	p.topo = -1;
	return p;
}

int pilhaVazia(Pilha p) {
	return (p.topo == -1);
}

void pushPilha(Pilha *p, int x) {
	p->topo++;
	p->vetor[p->topo] = x;
	return;
}

int popPilha(Pilha *p) {
	int x = p->vetor[p->topo];
	p->topo--;
	return x;
}

typedef struct noh{
	int vert;
	struct noh *prox;
}No;

typedef struct grafo{
	No** lista;
}Grafo;

Grafo criaGrafo(int n){
	int i;
	//cria ponteiro para uma estrutura de grafo
	Grafo* g = (Grafo*) malloc(sizeof(Grafo));
	//cria uma lista de ponteiros que apontam para as listas de adjacencia
	g->lista = (No**) malloc(sizeof(No*)*n);
	//guarda o inicio de cada uma das listas, sendo cada noh um dos vertices do grafo (0 a n-1)
	for(i = 0; i < n; i++){
		No* n = (No*) malloc(sizeof(No)); //alocando espaco de um no da lista ligada
		n->vert = i; //define o vertice
		n->prox = NULL; //proximo = NULL -> lista vazia
		g->lista[i] = n; //guarda o ponteiro no array de ponteiros do grafo
	}
	return (*g); //retorna o tad apontado pelo ponteiro de grafo
}

void insereAresta(Grafo *g, int v, int u){
	//cria um noh auxiliar com o valor de vertice v
	No* copia_v = (No*) malloc(sizeof(No));
	copia_v->vert = v;
	copia_v->prox = NULL;
	
	//cria um noh auxiliar com o valor de vertice u
	No* copia_u = (No*) malloc(sizeof(No));
	copia_u->vert = u;
	copia_u->prox = NULL;

	//cria um noh auxiliar que contem o inicio da lista ligada do vertice v
	No* aux = g->lista[v];
	while(aux->prox) aux = aux->prox;
	aux->prox = copia_u; //coloca u como sendo o ultimo da lista ligada de v

	//cria um noh auxiliar que contem o inicio da lista ligada do vertice v
	aux = g->lista[u];
	while(aux->prox) aux = aux->prox;
	aux->prox = copia_v; //coloca v como sendo o ultimo da lista ligada de u

	return;
}

int buscaProfundidade(Grafo g, int s){
	int visitados[MAX] = {0}; //cria array de vertices visitados com todos nao visitados
	int vertice, resultado = 0;
	Pilha p = criaPilha();

	pushPilha(&p, s); //insere o vertice source na pilha

	//printf("Busca em Profundidade:");

	while(!pilhaVazia(p)){ //enquanto a pilha tiver algum elemento
		vertice = popPilha(&p); //retira esse elemento
		if(!visitados[vertice]){ //olha se ele ja foi visitado, caso nao tenha sido:
			resultado += 2;
			visitados[vertice]++; //marca como visitado
			//printf(" %d", vertice); //imprime o vertice
			No* noh = g.lista[vertice]; //busca a sua lista de vertices adjacentes
			while(noh->prox){ //percorre a lista inserindo todos os elementos da mesma na pilha
				noh = noh->prox;
				pushPilha(&p, noh->vert);
			}
		}
		//repete o procedimento efetuando uma busca em profundidade
	}
	//printf("\n");
	return resultado-2;
}

int main(){
	int j, i, t, inicio, vert, arestas, x, y, result;
	scanf("%d", &t);
	for(i = 0; i < t; i++){
		scanf("%d", &inicio);
		scanf("%d %d", &vert, &arestas);
		Grafo g = criaGrafo(vert);
		for(j = 0; j < arestas; j++){
			scanf("%d %d", &x, &y);
			insereAresta(&g, x, y);
		}
		result = buscaProfundidade(g, inicio);
		printf("%d\n", result);
	}
}