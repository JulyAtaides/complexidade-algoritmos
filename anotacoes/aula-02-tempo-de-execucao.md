# Aula 2 - Tempo de execução e os casos

## O que eu preciso aprender aqui

- do que o tempo de execução depende
- por que a gente conta passos e não segundos
- melhor caso, pior caso e caso médio

---

## Do que o tempo depende

1. da **máquina** (computador, sistema, linguagem)
2. do **algoritmo**
3. do **tamanho da entrada** (n)

A máquina muda se eu trocar de computador, então não dá pra medir o algoritmo
em segundos. Por isso a gente **conta quantos passos** ele faz em função de n.
Assim o resultado é do algoritmo, não do computador.

## Pior caso

É o maior tempo que o algoritmo pode levar. É o que normalmente a gente
calcula, porque é uma garantia: nenhuma entrada vai demorar mais que isso.

- na busca: quando o elemento **não está** no vetor
- na ordenação por inserção: vetor em **ordem inversa**

## Melhor caso

Quando a entrada já está do jeito bom.

- na busca: acha logo na primeira posição
- na ordenação: vetor já ordenado

## Caso médio

Usa probabilidade. Precisa saber (ou imaginar) como os dados costumam vir, por
isso é menos usado.

## Os três casos rodando

Rodei a ordenação por inserção com n = 6
([insercao.py](../codigo/insercao.py)) e somei quantas vezes todas as linhas
rodaram:

| Caso | Vetor | Total |
|---|---|---|
| melhor | [1, 2, 3, 4, 5, 6] | 26 |
| qualquer | [4, 2, 3, 5, 1, 6] | 44 |
| pior | [6, 5, 4, 3, 2, 1] | 71 |

Mesmo tamanho de vetor e quase o triplo de trabalho só por causa da ordem dos
números.

## Onde eu me confundi

- Pensei que melhor caso era "n pequeno". Não é: o n é o mesmo, o que muda é
  como os dados estão arrumados.
