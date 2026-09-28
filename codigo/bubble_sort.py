# BubbleSort do capitulo 1, contando comparacoes e trocas.
#
# 1  para i de 1 ate n-1 faca
# 2      para j de 1 ate n-i faca
# 3          se A[j] > A[j+1] entao
# 4              trocar A[j] com A[j+1]
#
# Esse bubble nao tem aquela parada antecipada (quando nao troca nada),
# entao ele compara sempre a mesma quantidade.


def bubble_sort(vetor):
    A = list(vetor)
    n = len(A)
    comparacoes = 0
    trocas = 0

    for i in range(1, n):              # i de 1 ate n-1
        for j in range(0, n - i):      # j de 1 ate n-i (aqui comeca no 0)
            comparacoes += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                trocas += 1

    return A, comparacoes, trocas


if __name__ == "__main__":
    for vetor in ([1, 2, 3, 4, 5, 6], [4, 2, 3, 5, 1, 6], [6, 5, 4, 3, 2, 1]):
        ordenado, comp, trocas = bubble_sort(vetor)
        print(vetor, "->", ordenado, "| comparacoes:", comp, "| trocas:", trocas)

    n = 10
    print("\ncom n = 10 a formula n(n-1)/2 da:", n * (n - 1) // 2)
