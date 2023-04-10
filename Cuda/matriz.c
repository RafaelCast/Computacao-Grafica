/**
 * Vector addition: A = A + B.
 *
 * This sample is a very basic sample that implements element by element
 * vector addition. It is the same as the sample illustrating Chapter 2
 * of the programming guide with some additions like error checking.
 **/

#include <stdio.h>

// For the CUDA runtime routines (prefixed with "cuda_")


int main() {
    int n_rows, n_cols;

    printf("Digite o número de linhas da matriz: ");
    scanf("%d", &n_rows);

    printf("Digite o número de colunas da matriz: ");
    scanf("%d", &n_cols);

    // Criando matriz A com valores crescentes
    int **A = (int **)malloc(n_rows * sizeof(int *));
    for (int i = 0; i < n_rows; i++) {
        A[i] = (int *)malloc(n_cols * sizeof(int));
        for (int j = 0; j < n_cols; j++) {
            A[i][j] = i*n_cols + j + 1;
        }
    }

    // Criando matriz B com valores iguais a 2
    int **B = (int **)malloc(n_rows * sizeof(int *));
    for (int i = 0; i < n_rows; i++) {
        B[i] = (int *)malloc(n_cols * sizeof(int));
        for (int j = 0; j < n_cols; j++) {
            B[i][j] = 2;
        }
    }

    // Imprimindo matrizes A e B
    printf("Matriz A:\n");
    for (int i = 0; i < n_rows; i++) {
        for (int j = 0; j < n_cols; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }

    printf("Matriz B:\n");
    for (int i = 0; i < n_rows; i++) {
        for (int j = 0; j < n_cols; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }

    // Liberando memória alocada
    for (int i = 0; i < n_rows; i++) {
        free(A[i]);
        free(B[i]);
    }
    free(A);
    free(B);

    return 0;
}