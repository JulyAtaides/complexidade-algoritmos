# MergeSort e Intercala (nomes da professora), contando as comparacoes.
#
# MergeSort(A, inicio, fim)
# 1  se inicio < fim entao
# 2      meio = (inicio + fim) / 2
# 3      MergeSort(A, inicio, meio)
# 4      MergeSort(A, meio+1, fim)
# 5      Intercala(A, inicio, meio, fim)

comparacoes = 0


def intercala(A, inicio, meio, fim):
    global comparacoes
    B = []
    i = inicio
    j = meio + 1
    while i <= meio and j <= fim:
        comparacoes += 1
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    # o que sobrou de um dos lados ja esta em ordem, so copia
    B.extend(A[i:meio + 1])
    B.extend(A[j:fim + 1])
    A[inicio:fim + 1] = B


def merge_sort(A, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort(A, inicio, meio)
        merge_sort(A, meio + 1, fim)
        intercala(A, inicio, meio, fim)


def ordena(vetor):
    global comparacoes
    comparacoes = 0
    A = list(vetor)
    merge_sort(A, 0, len(A) - 1)
    return A, comparacoes


if __name__ == "__main__":
    for vetor in ([1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [1, 5, 3, 7, 2, 6, 4, 8]):
        ordenado, comp = ordena(vetor)
        print(vetor, "->", ordenado, "| comparacoes:", comp)
