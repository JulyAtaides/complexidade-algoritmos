# Aula 4 - Algoritmos de ordenação

Ordenação por inserção, BubbleSort e MergeSort. O código de cada um está na
pasta [codigo](../codigo).

## O que eu preciso aprender aqui

- a tabela da ordenação por inserção (é a análise modelo)
- por que o BubbleSort é O(n²) sempre
- como o MergeSort divide e junta
- comparar os três

---

## 1. Ordenação por inserção

```
Ordena-por-inserção (A, n)
1    for i = 2 to n
2        chave = A[i]
3        j = i − 1
4        while j > 0 e A[j] > chave
5            A[j+1] = A[j]
6            j = j − 1
7        A[j+1] = chave
```

Parece arrumar cartas na mão: pego uma carta e vou empurrando as maiores pra
direita até achar o lugar dela.

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | for i = 2 to n | c₁ | n |
| 2 | chave = A[i] | c₂ | n − 1 |
| 3 | j = i − 1 | c₃ | n − 1 |
| 4 | while j > 0 e A[j] > chave | c₄ | ∑ᵢ₌₂ⁿ tᵢ |
| 5 | A[j+1] = A[j] | c₅ | ∑ᵢ₌₂ⁿ (tᵢ − 1) |
| 6 | j = j − 1 | c₆ | ∑ᵢ₌₂ⁿ (tᵢ − 1) |
| 7 | A[j+1] = chave | c₇ | n − 1 |

- A linha 1 dá **n** e não n+1 porque o for começa no 2. O corpo roda n − 1
  vezes, e o teste uma a mais: n.
- tᵢ é quantas vezes o while é testado na volta i. Depende dos dados.

**Melhor caso (já ordenado):** o while testa uma vez e já sai, então tᵢ = 1.

```
T(n) = (c₁ + c₂ + c₃ + c₄ + c₇) n − (c₂ + c₃ + c₄ + c₇)
```

Forma an + b, função linear de n: **O(n)**.

**Pior caso (invertido):** cada elemento anda até o começo, então tᵢ = i.

```
T(n) = (c₄/2 + c₅/2 + c₆/2) n² + (c₁ + c₂ + c₃ + c₄/2 + c₅/2 + c₆/2 + c₇) n − (c₂ + c₃ + c₄ + c₇)
```

Forma an² + bn + c, função quadrática de n: **O(n²)**.

Rodando com n = 6:

| Linha | melhor | pior |
|---|---|---|
| 1 | 6 | 6 |
| 2 | 5 | 5 |
| 3 | 5 | 5 |
| 4 | 5 | 20 |
| 5 | 0 | 15 |
| 6 | 0 | 15 |
| 7 | 5 | 5 |

A linha 4 no pior caso deu 20 = 6·7/2 − 1, e as linhas 5 e 6 deram
15 = 6·5/2. Bateu com as fórmulas.

---

## 2. BubbleSort

```
ALGORITMO BubbleSort(A, n)
1    para i de 1 até n-1 faça
2        para j de 1 até n-i faça
3            se A[j] > A[j+1] então
4                trocar A[j] com A[j+1]
5            fim se
6        fim para
7    fim para
```

A cada passada o maior "sobe" pro fim, igual bolha.

Comparações:

```
(n−1) + (n−2) + ... + 1 = n(n−1)/2
```

Com n = 10 dá 45.

O que me surpreendeu rodando o código: com n = 6 ele fez **15 comparações nos
três casos** (ordenado, bagunçado e invertido). Só as trocas mudaram (0, 6 e
15). Esse BubbleSort não tem a parada antecipada, então mesmo com o vetor já
ordenado ele compara tudo. É **O(n²) sempre**.

---

## 3. MergeSort e Intercala

```
ALGORITMO MergeSort(A, inicio, fim)
1    se inicio < fim então
2        meio <- (inicio + fim) / 2
3        MergeSort(A, inicio, meio)
4        MergeSort(A, meio+1, fim)
5        Intercala(A, inicio, meio, fim)
6    fim se
```

- divide o vetor no meio
- ordena cada metade (chamando ele mesmo)
- o **Intercala** junta as duas metades já ordenadas

O Intercala compara o primeiro de cada metade, copia o menor e anda. Quando
uma metade acaba, o resto da outra só é copiado.

Fórmulas de comparação do capítulo 1:

```
pior caso:   ≈ n·log₂(n) − n + 1
melhor caso: ≈ n·log₂(n) / 2
```

Testei com n = 8 ([merge_sort.py](../codigo/merge_sort.py)):

| Vetor | Comparações |
|---|---|
| ordenado [1..8] | 12 |
| invertido [8..1] | 12 |
| [1, 5, 3, 7, 2, 6, 4, 8] | 17 |

Achei que o invertido seria o pior, igual na inserção, mas não! No invertido
cada metade é toda maior que a outra, então o Intercala esvazia um lado
rápido. O pior é quando as metades ficam se alternando. E 17 = 8·3 − 8 + 1,
bate com a fórmula do pior caso.

---

## Comparando os três

| Algoritmo | Melhor caso | Pior caso |
|---|---|---|
| Inserção | O(n) | O(n²) |
| BubbleSort | O(n²) | O(n²) |
| MergeSort | O(n log n) | O(n log n) |

Cenário da professora com n = 1.000.000: o BubbleSort faz 499.999.500.000
comparações e o MergeSort, no pior caso, mais ou menos 18.931.569. É muita
diferença.

## Onde eu me confundi

- Linha 1 da inserção: coloquei n + 1. É n porque o for começa no 2.
- Achei que BubbleSort com vetor ordenado seria rápido. Não é, sem parada
  antecipada ele compara tudo.
- Achei que o vetor invertido era o pior caso do MergeSort. Não é.
