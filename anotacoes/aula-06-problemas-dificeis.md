# Aula 6 - Problemas difíceis (NP-completos)

## O que eu preciso aprender aqui

- o que é um problema NP-completo
- os dois exemplos do capítulo: Caixeiro Viajante e Mochila
- por que eles são tão mais difíceis que O(n²)

---

## O que são

São problemas que ninguém conhece um algoritmo eficiente pra resolver. Mas
também **ninguém provou que não existe**. É uma pergunta em aberto.

E eles são ligados: se alguém achar um jeito eficiente de resolver um, dá pra
resolver todos.

## Caixeiro Viajante

Achar o caminho mais curto que passa por todas as cidades.

Com 20 cidades são 20! caminhos, mais ou menos 2,4 × 10¹⁸. Testando um bilhão
de caminhos por segundo, ia levar uns 76 anos.

| Cidades | Caminhos |
|---|---|
| 5 | 120 |
| 10 | 3.628.800 |
| 20 | 2.432.902.008.176.640.000 |

## Mochila

Tenho itens com peso e valor e uma mochila com limite. Quais itens levar pra
ter o maior valor?

Cada item entra ou não entra, então são 2ⁿ combinações.

| Itens | Combinações |
|---|---|
| 10 | 1.024 |
| 20 | 1.048.576 |
| 30 | 1.073.741.824 |

## Por que é outra coisa

| | n = 20 | n = 50 |
|---|---|---|
| n² | 400 | 2.500 |
| 2ⁿ | 1.048.576 | 1.125.899.906.842.624 |

O(n²) fica lento. O(2ⁿ) fica impossível. Não adianta comprar computador
melhor.

## Onde eu me confundi

- Escrevi que "está provado que não tem solução eficiente". Não está provado,
  ninguém sabe ainda.
