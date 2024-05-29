#include <stdio.h>

/**
* appand_arr- a func that add the first arry to the second
* @A: pointer to tha array A
* @B: pointer to the array B
* @N: the length of the array A
* @M: the length of the array B
**/

void appand_arr(int *A, int *B, int N, int M) {
    A += N;

    for (int i = 0; i < M; i++) {
        *A = *B;
        A++;
        B++;
    }
}

int main() {
    int N, M;

    printf("Enter the size of array A: ");
    scanf("%d", &N);

    printf("Enter the elements of array A:\n");
    int A[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    printf("Enter the size of array B: ");
    scanf("%d", &M);

    printf("Enter the elements of array B:\n");
    int B[M];
    for (int i = 0; i < M; i++) {
        scanf("%d", &B[i]);
    }

    appand_arr(A, B, N, M);

    printf("Combined array A:\n");
    for (int i = 0; i < N + M; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");

    return 0;
}
