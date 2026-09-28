# Busca linear e busca binaria, contando quantas voltas cada uma da.


def busca_linear(A, x):
    voltas = 0
    for i in range(len(A)):
        voltas += 1
        if A[i] == x:
            return i, voltas
    return "nao encontrado", voltas


def busca_binaria(A, x):
    # so funciona certo se A estiver em ordem!
    esq = 0
    dir = len(A) - 1
    voltas = 0
    while esq <= dir:
        voltas += 1
        meio = (esq + dir) // 2
        if A[meio] == x:
            return meio, voltas
        elif A[meio] < x:
            esq = meio + 1
        else:
            dir = meio - 1
    return "nao encontrado", voltas


def encontra_maior_errado(A):
    maior = 0            # erro: e se todo mundo for negativo?
    for v in A:
        if v > maior:
            maior = v
    return maior


def encontra_maior_certo(A):
    maior = A[0]         # comeca com um valor que existe no vetor
    for v in A[1:]:
        if v > maior:
            maior = v
    return maior


if __name__ == "__main__":
    for n in (16, 1024, 1048576):
        A = list(range(1, n + 1))
        _, lin = busca_linear(A, n + 1)      # procuro algo que nao existe
        _, bin_ = busca_binaria(A, n + 1)
        print(f"n = {n}: linear {lin} voltas, binaria {bin_} voltas")

    negativos = [-5, -2, -8, -1]
    print("\nmaior de", negativos)
    print("  versao errada:", encontra_maior_errado(negativos))
    print("  versao certa:", encontra_maior_certo(negativos))

    desordenado = [7, 1, 9, 3, 5]
    # o 1 esta no vetor, mas como ele nao esta em ordem a binaria nao acha
    print("\nbinaria procurando 1 em", desordenado, "->", busca_binaria(desordenado, 1)[0])
