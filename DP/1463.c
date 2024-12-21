#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int min(int a, int b){
    return (a < b) ? a : b;
}

int make_one(int num)
{
    if(num < 2)
        return 0;
    int* L = (int*)malloc(sizeof(int) * (num+1));
    memset(L, 0, sizeof(L));

    for(int i=2; i<num+1; i++){
        L[i] = 1 + L[i-1];
        if(i % 2 == 0)
            L[i] = min(L[i], L[i / 2] + 1);
        if(i % 3 == 0)
            L[i] = min(L[i], L[i / 3] + 1);
    }
        
    return L[num];
}
    
int main(void){
    int N;
    scanf("%d", &N);
    int ops = make_one(N);
    printf("%d\n", ops);
    return 0;
}