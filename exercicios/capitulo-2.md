# Exercícios do Capítulo 2

Primeiro os 4 que a professora resolveu na apostila (refiz pra treinar) e
depois os 4 propostos, que não têm gabarito, então a resolução é minha.

Pra conferir os números dos propostos eu rodei
[exercicios_cap2.py](../codigo/exercicios_cap2.py), que conta quantas vezes
cada linha roda.

---

## Parte 1 - Resolvidos na apostila

### 1. Soma-dois-numeros

```
1    x = 5
2    y = x * 2
3    retorne x + y
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | x = 5 | c₁ | 1 |
| 2 | y = x * 2 | c₂ | 1 |
| 3 | retorne x + y | c₃ | 1 |

T(n) = c₁ + c₂ + c₃ = 3. Constante: **O(1)**.

### 2. Soma-numeros-vetor

```
1    Soma = 0
2    for i de 1 to n faça
3        soma = soma + A[i]
4    retorne soma
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | Soma = 0 | c₁ | 1 |
| 2 | for i de 1 to n faça | c₂ | n + 1 |
| 3 | soma = soma + A[i] | c₃ | n |
| 4 | retorne soma | c₄ | 1 |

T(n) = 1 + (n + 1) + n + 1 = 2n + 3. Função linear de n: **O(n)**.

### 3. Soma-de-laços-aninhados

```
1    for i de 1 to n faça
2        for j de 1 to n faça
3            total = total + 1
4    retorne soma
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | for i de 1 to n faça | c₁ | n + 1 |
| 2 | for j de 1 to n faça | c₂ | n(n + 1) |
| 3 | total = total + 1 | c₃ | n · n |
| 4 | retorne soma | c₄ | 1 |

T(n) = (n + 1) + (n² + n) + n² + 1 = 2n² + 2n + 2. Função quadrática de n:
**O(n²)**.

A linha 2 foi onde eu errei na primeira vez: o for de dentro é testado n + 1
vezes **em cada volta** do de fora, então é n(n + 1).

### 4. Laço-divide-ao-meio

```
1    i = n
2    enquanto i > 1 faça
3        i = i / 2
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | i = n | c₁ | 1 |
| 2 | enquanto i > 1 faça | c₂ | log₂n + 1 |
| 3 | i = i / 2 | c₃ | log₂n |

Função logarítmica de n: **O(log n)**. Com n = 8: 8, 4, 2, 1, são 3 passos, e
log₂8 = 3.

---

## Parte 2 - Propostos (resolução minha)

### 1. Calcula-média

```
1    a = 10
2    b = 20
3    média = (a + b) / 2
4    retorna média
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | a = 10 | c₁ | 1 |
| 2 | b = 20 | c₂ | 1 |
| 3 | média = (a + b) / 2 | c₃ | 1 |
| 4 | retorna média | c₄ | 1 |

T(n) = 4. Não tem laço e não depende de n: **O(1)**.

### 2. Conta-elementos

```
1    contador = 0
2    for i de 1 to n faça
3        se A[i] é par então
4            contador = contador + 1
5    retorna contador
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | contador = 0 | c₁ | 1 |
| 2 | for i de 1 to n faça | c₂ | n + 1 |
| 3 | se A[i] é par então | c₃ | n |
| 4 | contador = contador + 1 | c₄ | p (quantidade de pares) |
| 5 | retorna contador | c₅ | 1 |

A linha 4 depende de quantos pares tem.

- pior caso, todos pares (p = n): T(n) = 3n + 3
- melhor caso, nenhum par (p = 0): T(n) = 2n + 3

Os dois são função linear de n: **O(n)**.

Conferi com o vetor [1, 2, 3, 4, 5, 6, 7, 8] (4 pares): deu 1, 9, 8, 4 e 1,
total 23. Pela fórmula: 1 + 9 + 8 + 4 + 1 = 23.

### 3. Soma-matriz

```
1    soma = 0
2    for i de 1 to n faça
3        for j de 1 to n faça
4            soma = soma + M[i][j]
5    retorna soma
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | soma = 0 | c₁ | 1 |
| 2 | for i de 1 to n faça | c₂ | n + 1 |
| 3 | for j de 1 to n faça | c₃ | n(n + 1) |
| 4 | soma = soma + M[i][j] | c₄ | n² |
| 5 | retorna soma | c₅ | 1 |

T(n) = 1 + (n + 1) + (n² + n) + n² + 1 = 2n² + 2n + 3. Função quadrática de n:
**O(n²)**.

É quase igual ao resolvido 3. Conferi com n = 8: 1 + 9 + 72 + 64 + 1 = 147, e
2·64 + 2·8 + 3 = 147.

### 4. Contador-que-reduz

```
1    contador = 0
2    enquanto n > 1 faça
3        n = n / 2
4        contador = contador + 1
5    retorna contador
```

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|
| 1 | contador = 0 | c₁ | 1 |
| 2 | enquanto n > 1 faça | c₂ | log₂n + 1 |
| 3 | n = n / 2 | c₃ | log₂n |
| 4 | contador = contador + 1 | c₄ | log₂n |
| 5 | retorna contador | c₅ | 1 |

T(n) = 3·log₂n + 3. Função logarítmica de n: **O(log n)**.

Com n = 16 o laço rodou 4 vezes (16, 8, 4, 2 e parou no 1), e log₂16 = 4.
Quando n não é potência de 2 arredonda pra baixo: com n = 33 deu 5 voltas.

---

## Resumo

| Exercício | T(n) | O |
|---|---|---|
| Soma-dois-numeros | 3 | O(1) |
| Soma-numeros-vetor | 2n + 3 | O(n) |
| Soma-de-laços-aninhados | 2n² + 2n + 2 | O(n²) |
| Laço-divide-ao-meio | log₂n + 1 voltas no teste | O(log n) |
| Calcula-média | 4 | O(1) |
| Conta-elementos | 3n + 3 (pior) | O(n) |
| Soma-matriz | 2n² + 2n + 3 | O(n²) |
| Contador-que-reduz | 3·log₂n + 3 | O(log n) |
