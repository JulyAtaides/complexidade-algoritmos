# Conta quantas vezes cada linha roda nos exercicios propostos do capitulo 2.
# Uso pra conferir as tabelas que eu fiz na mao.


def conta_elementos(A):
    v = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    contador = 0
    v[1] += 1
    for i in range(len(A) + 1):      # +1 por causa do teste final
        v[2] += 1
        if i == len(A):
            break
        v[3] += 1
        if A[i] % 2 == 0:
            contador += 1
            v[4] += 1
    v[5] += 1
    return contador, v


def soma_matriz(n):
    M = [[1] * n for _ in range(n)]
    v = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    soma = 0
    v[1] += 1
    for i in range(n + 1):
        v[2] += 1
        if i == n:
            break
        for j in range(n + 1):
            v[3] += 1
            if j == n:
                break
            soma += M[i][j]
            v[4] += 1
    v[5] += 1
    return soma, v


def contador_que_reduz(n):
    v = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    contador = 0
    v[1] += 1
    while True:
        v[2] += 1
        if not n > 1:
            break
        n = n // 2
        v[3] += 1
        contador += 1
        v[4] += 1
    v[5] += 1
    return contador, v


if __name__ == "__main__":
    _, v = conta_elementos([1, 2, 3, 4, 5, 6, 7, 8])
    print("Conta-elementos com [1..8]:", v, "total", sum(v.values()))

    _, v = soma_matriz(8)
    print("Soma-matriz com n = 8:", v, "total", sum(v.values()))

    for n in (8, 16, 33):
        c, v = contador_que_reduz(n)
        print(f"Contador-que-reduz com n = {n}: {c} voltas, total {sum(v.values())}")
