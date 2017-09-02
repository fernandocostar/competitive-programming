// Desafios de Programação - Tarefa 10a
// Fernando Mendes

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool estaoJuntas(int xI1, int xF1, int xI2, int xF2){
  if(xI1 <= xI2){
    if(xI2 <= xF1){
      return true;
    }
  }else{
    if(xI1 <= xF2){
      return true;
    }
  }
  return false;
}


int main(){
  // variaveis
  int numP = 0;
  int xMax = 0;
  cin >> dec >> numP;

  vector <int> xI(numP, 0);
  vector <int> xF(numP, 0);
  vector <int> alt(numP, 0);


for (size_t i = 0; i < numP; i++) {
  cin >> dec >> xI[i] >> dec >> alt[i] >> dec >> xF[i];
}
std::vector<int> aux(xF);
sort (aux.begin(), aux.end());
xMax = aux[numP-1];
cout << aux[numP-1] << '\n';

vector < int > resposta(xMax-1, 0);



for (size_t n = 0; n < numP; n++) {

  for (size_t i = xI[n]-1; i < xF[n]-1; i++) {
    if(resposta[i] < alt[n]){
      resposta[i] = alt[n];
    }
    }
  }

//teste
for (size_t i = 0; i < xMax; i++) {
  if(resposta[i] != resposta[i-1]){
    cout << i << " " << resposta[i] << '\n';
  }
}

//for (size_t i = 0; i < xMax; i++) {
//    cout << resposta [i] << " - ";
//}

  return 0;
}
