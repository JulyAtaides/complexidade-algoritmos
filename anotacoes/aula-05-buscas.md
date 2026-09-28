# Aula 5 - Busca linear e busca binária

## O que eu preciso aprender aqui

- as duas buscas e o custo de cada uma
- por que a binária precisa do vetor em ordem
- provar que a binária é correta (exercício do capítulo 1)

---

## Busca linear

```
BuscaLinear(A, n, x)
1    para i de 1 até n faça
2        se A[i] = x então
3            retorne i
4    retorne "não encontrado"
```

Olha um por um.

**Pior caso** (x não está no vetor):

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | para i de 1 até n faça | c₁ | n + 1 |
| 2 | se A[i] = x então | c₂ | n |
| 3 | retorne i | c₃ | 0 |
| 4 | retorne "não encontrado" | c₄ | 1 |

T(n) = (c₁ + c₂) n + (c₁ + c₄). Função linear de n: **O(n)**.

**Melhor caso** (achou na primeira): a linha 1 roda só **1 vez**, não 2,
porque ele sai pelo `retorne` e não faz o último teste. **O(1)**.

## Busca binária

```
BuscaBinaria(A, n, x)
1    esq <- 1
2    dir <- n
3    enquanto esq <= dir faça
4        meio <- (esq + dir) / 2
5        se A[meio] = x então
6            retorne meio
7        senão se A[meio] < x então
8            esq <- meio + 1
9        senão
10           dir <- meio - 1
11   retorne "não encontrado"
```

Olha o meio. Se o x é maior, joga fora a metade da esquerda. Se é menor, joga
fora a da direita. Cada volta corta o vetor pela metade, então é **O(log n)**.

Rodei procurando um número que não existe
([buscas.py](../codigo/buscas.py)):

| n | linear | binária |
|---|---|---|
| 16 | 16 voltas | 5 voltas |
| 1.024 | 1.024 voltas | 11 voltas |
| 1.048.576 | 1.048.576 voltas | 21 voltas |

Mais de um milhão de números e a binária resolveu em 21 voltas.

## A binária é correta? (exercício do capítulo 1)

Gabarito da professora: é correta. Termina porque o intervalo [esq, dir]
diminui pela metade a cada volta e o laço acaba quando esq > dir. E o vetor
estar ordenado é essencial.

Separando nas duas partes de "correto":

- **Para:** o intervalo sempre diminui, porque usa meio + 1 e meio − 1.
- **Resposta certa:** só se o vetor estiver em ordem. Ela joga fora metade
  achando que ali só tem número menor (ou maior). Se o vetor estiver bagunçado,
  pode jogar fora justamente o que eu procuro.

Testei isso: procurei o 1 em [7, 1, 9, 3, 5] e a binária respondeu "não
encontrado", mesmo o 1 estando lá. Ela não trava, ela só responde errado.

## Onde eu me confundi

- Coloquei n + 1 na linha 1 da linear no melhor caso. Quando sai pelo retorne
  não tem o teste final.
- Achei que a binária "dava erro" em vetor bagunçado. Ela roda normal, só que
  responde errado.
