# Aula 3 - Contando passos: tabela, T(n) e notação O

Capítulo 2. É a aula mais importante pra prova, porque é o jeito que a
professora quer a resolução.

## O que eu preciso aprender aqui

- montar a tabela do jeito dela
- a regra do laço (uma vez a mais)
- transformar laço em somatória
- escrever o T(n)
- simplificar e dar a notação O

---

## A tabela da professora

Sempre 4 colunas:

| Linha | Instrução | Custo | Vezes |
|---|---|---|---|

- **Custo**: c₁, c₂, c₃... com c minúsculo. Começa de novo no c₁ em cada
  algoritmo.
- **Vezes**: quantas vezes aquela linha roda, em função de n.
- `fim se`, `fim para`, `senão` e comentário entram na tabela mas o custo é
  **—** (não custam nada).
- Não tem coluna de "custo total". A multiplicação vai no T(n).

## A regra do laço

Nas palavras dela, os laços "são executados uma vez mais do que as instruções
que estão dentro deles, pois há o teste final que não cumpre mais os
requisitos".

```
for i de 1 to n faça     ->  n + 1 vezes
    corpo                ->  n vezes
```

Eu penso assim: pra sair do laço, alguém tem que testar e ver que acabou. Esse
teste também conta.

**Cuidado:** se o laço sai por um `retorne` lá de dentro, esse último teste não
acontece.

## Quando vira somatória

Se o laço de dentro roda uma quantidade diferente a cada volta do de fora, a
coluna Vezes vira somatória.

A fórmula que resolve quase tudo (soma de Gauss):

```
1 + 2 + 3 + ... + n = n(n+1)/2
```

E as duas variações que aparecem na ordenação por inserção:

```
2 + 3 + ... + n       = n(n+1)/2 - 1     (é a de cima sem o 1)
1 + 2 + ... + (n-1)   = n(n-1)/2
```

Conferi com n = 6: n(n+1)/2 - 1 = 20 e n(n-1)/2 = 15. São exatamente os
números da linha 4 e das linhas 5 e 6 no pior caso da inserção (ver
[aula 4](aula-04-ordenacao.md)).

## Laço que divide por 2

```
i = n
enquanto i > 1 faça
    i = i / 2
```

Exemplo dela: com n = 8, o i vale 8, 4, 2, 1. São 3 passos, e log₂8 = 3.
Então esse laço roda **log₂ n** vezes.

## T(n)

É a soma de custo × vezes de cada linha:

```
T(n) = c₁ * (vezes da linha 1) + c₂ * (vezes da linha 2) + ...
```

## Simplificar e dar o O

A professora faz nessa ordem:

1. junta as constantes até ficar numa forma simples
2. fala o nome da forma
3. só depois escreve o O

| Forma | Nome | O |
|---|---|---|
| número fixo | constante | O(1) |
| an + b | função linear de n | O(n) |
| an² + bn + c | função quadrática de n | O(n²) |
| log₂ n | logarítmica | O(log n) |

As constantes (os c) somem porque dependem da máquina. O que importa é como o
tempo cresce quando n cresce.

Atalho pra reconhecer rápido (mas na prova tem que mostrar a conta):

- sem laço: O(1)
- um laço de 1 em 1: O(n)
- dois laços um dentro do outro: O(n²)
- laço que divide por 2: O(log n)

## Se n dobrar

| O | o tempo... |
|---|---|
| O(1) | não muda |
| O(log n) | aumenta só 1 passo |
| O(n) | dobra |
| O(n²) | fica 4 vezes maior |

## Onde eu me confundi

- Esqueci o +1 do laço várias vezes. Agora eu sempre olho a linha do `for`
  separada do corpo.
- Coloquei custo no `fim se`. É —.
- Fui direto no O(n²) sem mostrar a forma an² + bn + c. Ela quer a forma
  antes.
- Usei n(n+1)/2 onde era n(n+1)/2 - 1 (a soma começava no 2).
