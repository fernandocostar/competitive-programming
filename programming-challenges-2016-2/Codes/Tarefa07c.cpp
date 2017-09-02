#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	string anagrama;
	cin >> anagrama;
	while(anagrama.compare("#") != 0){
		if(next_permutation(anagrama.begin(), anagrama.end())){
			cout << anagrama << "\n";
		}else{
			cout << "inexistente" << "\n";
		}
		cin >> anagrama;
	}
	return 0;
}