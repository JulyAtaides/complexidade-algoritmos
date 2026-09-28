# Ordenacao por insercao, contando quantas vezes cada linha roda.
#
# Pseudocodigo da professora (capitulo 2):
# 1  for i = 2 to n
# 2      chave = A[i]
# 3      j = i - 1
# 4      while j > 0 e A[j] > chave
# 5          A[j+1] = A[j]
# 6          j = j - 1
# 7      A[j+1] = chave
#
# Em Python a lista comeca no 0, entao eu coloquei um None na posicao 0
# pra poder usar os mesmos indices do pseudocodigo (1 ate n).


def ordena_por_insercao(vetor):
    A = [None] + list(vetor)
    n = len(vetor)
    vezes = {linha: 0 for linha in range(1, 8)}

    i = 2
    while True:
        vezes[1] += 1              # teste do for (roda uma vez a mais)
        if i > n:
            break
        chave = A[i]
        vezes[2] += 1
        j = i - 1
        vezes[3] += 1
        while True:
            vezes[4] += 1          # teste do while
            if not (j > 0 and A[j] > chave):
                break
            A[j + 1] = A[j]
            vezes[5] += 1
            j = j - 1
            vezes[6] += 1
        A[j + 1] = chave
        vezes[7] += 1
        i += 1

    return A[1:], vezes


if __name__ == "__main__":
    casos = {
        "melhor caso (ja ordenado)": [1, 2, 3, 4, 5, 6],
        "caso qualquer": [4, 2, 3, 5, 1, 6],
        "pior caso (invertido)": [6, 5, 4, 3, 2, 1],
    }
    for nome, vetor in casos.items():
        ordenado, vezes = ordena_por_insercao(vetor)
        print(nome, vetor, "->", ordenado)
        for linha, v in vezes.items():
            print(f"  linha {linha}: {v} vezes")
        print("  total:", sum(vezes.values()))
        print()
