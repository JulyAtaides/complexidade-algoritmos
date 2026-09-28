# Exercícios do Capítulo 1

Os dois exercícios propostos. Os dois têm gabarito na apostila, então eu
coloquei a minha resposta e conferi com o gabarito.

---

## Exercício 1 - A BuscaBinaria é correta?

### Enunciado

```
Verifique se o algoritmo BuscaBinaria é correto:

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

### Minha resposta

Pra ser correto ele tem que **parar** e dar a **resposta certa**.

1. **Ele para.** A cada volta o pedaço entre esq e dir fica menor, porque o esq
   vai pra meio + 1 ou o dir vai pra meio − 1. Uma hora esq passa do dir e o
   laço acaba.
2. **Dá a resposta certa, mas só se o vetor estiver ordenado.** Quando
   A[meio] < x, ele descarta a esquerda inteira. Isso só pode porque, em vetor
   ordenado, tudo que está à esquerda é menor que x.

Então: **é correto, desde que o vetor esteja em ordem.**

### Gabarito

É correto: termina porque o intervalo [esq, dir] é reduzido pela metade a cada
iteração e o laço acaba quando esq > dir. A condição de o vetor estar ordenado
é essencial para a correção.

Bateu com a minha resposta.

---

## Exercício 2 - Algoritmo, programa ou instância?

### Enunciado

```
Classifique cada item como algoritmo, programa ou instância de problema:
a) código Python da ordenação por inserção
b) "compare os dois números e exiba o maior"
c) vetor [5, 3, 8, 1] de entrada
d) implementação Java de Dijkstra
```

### Minha resposta

| Item | Resposta | Por quê |
|---|---|---|
| a | programa | está escrito em Python |
| b | algoritmo | é a explicação da lógica, sem linguagem |
| c | instância | é o dado de entrada |
| d | programa | está escrito em Java |

### Gabarito

a) Programa, b) Algoritmo, c) Instância de problema, d) Programa.

Bateu. O que eu quase errei foi o c: o vetor não é "o problema de ordenar", é
só um caso (instância) dele.
