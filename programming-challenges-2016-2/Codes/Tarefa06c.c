#include <stdio.h>
#include <stdlib.h>



int poda(int n){
    while(n%10==0){
        n/=10;
    }
    n=n%1000;
    return n;
}
int fatorial(int n){
    int num=1;
    int i;
    for(i=n;i>=1;i--){
        num = num*i;
        num= poda(num);
    }
    return num;
}
int main()
{
    int num, result;
    scanf("%d", &num);
    while(num != 0){
        result = fatorial(num);
        result = result%10;
        printf("%d\n", result);
        scanf("%d", &num);
    }

    return 0;
}
