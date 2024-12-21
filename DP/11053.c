#include <stdio.h>
#include <stdlib.h>

int max(int* A, int n)
{
    int max_value = 0;
    for(int i=0; i<n; i++){
        if(A[i] > max_value)
            max_value = A[i];
    }
    return max_value;
}

int lis(int* arr, int N)
{
    int* L = (int*)malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++) {
        L[i] = 1;
    }

    for(int i=1; i<N; i++){
        int* S = (int*)malloc(sizeof(int) * i);
        int count = 0;
        for(int j=0; j<i; j++){
            if(arr[j] < arr[i]){
                S[j] = L[j];
                count++;
            }else{
                S[j] = -1;
            }
        }
        if(count > 0)
            L[i] = 1 + max(S, i);
        else
            L[i] = 1;
        free(S);
    }

    return max(L, N);
}

int main(void){
    int N;
    scanf("%d", &N);
    int* arr = (int*)malloc(sizeof(int) * N);

    for(int i=0; i<N; i++)
        scanf("%d", &arr[i]);
    
    int res = lis(arr, N);
    printf("%d\n", res);
}