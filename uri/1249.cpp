#include <stdio.h>

using namespace std;

int main(){
    char c;
    int i;
    while(scanf("%c", &c) != EOF){
        if(c >= 'A' && c <= 'Z'){
            if(c + 13 <= 'Z') printf("%c", c + 13);
            else printf("%c", (c + 13)-26);
        }else if(c >= 'a' && c <= 'z'){
            if(c + 13 <= 'z') printf("%c", c += 13);
            else printf("%c", (c + 13) - 26);
        }else{
            printf("%c", c);
        }
    }
    return 0;
}