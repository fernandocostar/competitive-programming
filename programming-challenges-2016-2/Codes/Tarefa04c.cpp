// Tarefa 04b - Desafios de Programação


#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


// Busca da Esquerda para Direita
bool buscaHorizontalDireita(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){


  if( palavra.size() > matrizPalavras[0].size() - colInicio ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      colInicio++;
    }else{
      return false;
    }
  }
  return true;
}


// Busca da Direita para Esquerda
bool buscaHorizontaEsquerda(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){

  if( palavra.size() > colInicio+1 ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      colInicio--;
    }else{
      return false;
    }
  }
  return true;
}

// Busca de Cima para Baixo
bool buscaVerticalBaixo(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){

  if( palavra.size() > matrizPalavras.size() - linInicio ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      linInicio++;
    }else{
      return false;
    }
  }
  return true;


}

// Busca Baixo para Cima
bool buscaVerticalCima(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){

  if( palavra.size() > linInicio+1 ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      linInicio--;
    }else{
      return false;
    }
  }
  return true;


}

// Busca Diagonal da Direita para Esquerda, de Cima para Baixo
bool buscaDiagonalDireitaBaixo(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){

  if( palavra.size() > matrizPalavras[0].size() - colInicio || palavra.size() > matrizPalavras.size() - linInicio ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      linInicio++;
      colInicio++;
    }else{
      return false;
    }
  }
  return true;
}

// Busca Diagonal da Direita para Esquerda, de Baixo para Cima
bool buscaDiagonalDireitaCima(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){

  if( palavra.size() > matrizPalavras[0].size() - colInicio || palavra.size() > linInicio+1 ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      linInicio--;
      colInicio++;
    }else{
      return false;
    }
  }
  return true;
}

// Busca Diagonal da Esquerda para a Direita, de Cima para Baixo
bool buscaDiagonalEsquerdaBaixo(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){

  if( palavra.size() > colInicio+1 || palavra.size() > matrizPalavras.size() - linInicio ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      linInicio++;
      colInicio--;
    }else{
      return false;
    }
  }
  return true;
}

// Busca Diagonal da Direita para Esquerda, de Baixo para Cima
bool buscaDiagonalEsquerdaCima(vector< vector<char> >& matrizPalavras, string palavra, int linInicio, int colInicio){

  if( palavra.size() > colInicio+1 || palavra.size() > linInicio+1 ){
    return false;
  }

  vector<char> vPalavra(palavra.begin(), palavra.end());

  for (size_t i = 0; i < vPalavra.size(); i++) {
    if(vPalavra[i] == matrizPalavras[linInicio][colInicio]){
      linInicio--;
      colInicio--;
    }else{
      return false;
    }
  }
  return true;
}


bool buscaDiagonal(){



}



int main(){
  int numTestes = 0,
      tamLin = 0,
      tamCol = 0,
      numPalavras = 0,
      numBuscas = 0;

  string palavra,
         teste;

  bool encontrou = false;

  vector<int> result;





  // Usuario entra com o numero de testes a serem realizados
  cin >> numTestes;

  for (size_t i = 0; i < numTestes; i++) {

    // Usuario entra com a dimensao da matriz
    cin >> dec >> tamLin >> dec >> tamCol;

    // Cria matriz  vazia com o tamanho passado pelo usuario
    vector< vector<char> > matrizPalavras(tamLin, vector<char>(tamCol));

    // Preeenche a matriz de acordo com o conteudo digitado pelo usuario
    for (size_t j = 0; j < tamLin; j++) {

      cin >> palavra;
      transform(palavra.begin(), palavra.end(), palavra.begin(), ::tolower);
      vector<char> palavraV(palavra.begin(), palavra.end());

      matrizPalavras[j] = palavraV;

    }

    // Usuario diz quantas palavras vão ser buscadas
    cin >> numBuscas;

    // Cria vetor para testes
    vector<string> buscas(numBuscas);

    // Lê os testes a serem realizados
    for (size_t i = 0; i < numBuscas; i++) {
      cin >> teste;
      transform(teste.begin(), teste.end(), teste.begin(), ::tolower);
      buscas[i] = teste;
    }

    for (size_t i = 0; i < numBuscas; i++) {
      for (size_t j = 0; j < tamLin; j++) {
        for (size_t k = 0; k < tamCol; k++) {

          if (matrizPalavras[j][k] == buscas[i][0]) {


            encontrou = buscaHorizontaEsquerda(matrizPalavras, buscas[i], j, k) ||
                        buscaHorizontalDireita(matrizPalavras, buscas[i], j, k) ||
                        buscaVerticalBaixo(matrizPalavras, buscas[i], j, k) ||
                        buscaVerticalCima(matrizPalavras, buscas[i], j, k) ||
                        buscaDiagonalDireitaBaixo(matrizPalavras, buscas[i], j, k) ||
                        buscaDiagonalDireitaCima(matrizPalavras, buscas[i], j, k) ||
                        buscaDiagonalEsquerdaBaixo(matrizPalavras, buscas[i], j, k) ||
                        buscaDiagonalEsquerdaCima(matrizPalavras, buscas[i], j, k);


            if(encontrou == true){
              cout << j+1 << " "<< k+1 << '\n';
              encontrou = false;
            }
          }
        }
      }
    }


    //cout << '\n';
  }

}
