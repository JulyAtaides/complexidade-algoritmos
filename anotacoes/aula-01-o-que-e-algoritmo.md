# Aula 1 - O que é um algoritmo

Capítulo 1 da apostila. Primeira aula da matéria.

## O que eu preciso aprender aqui

- a definição de algoritmo
- as 5 características
- o que é instância
- a diferença entre algoritmo, programa e instância
- quando um algoritmo é correto

---

## Definição

Algoritmo é um procedimento computacional bem definido que recebe valores de
entrada e produz valores de saída, em um tempo finito.

Do jeito que eu entendi: é uma receita. Recebe os ingredientes (entrada),
segue passos claros e entrega o prato pronto (saída). E a receita tem que
acabar em algum momento.

## As 5 características

1. **Finito** - termina depois de um número finito de passos.
2. **Definido** - cada passo é claro, sem dar pra entender de dois jeitos.
3. **Entrada** - recebe zero ou mais valores.
4. **Saída** - produz pelo menos uma saída.
5. **Eficácia** - os passos são simples o bastante pra uma pessoa fazer com
   lápis e papel.

Anotei com atenção a 3 e a 4: a entrada pode ser **zero**, mas a saída tem que
ser **pelo menos uma**. Eu tinha escrito ao contrário na primeira vez.

## Instância

Instância é o dado concreto que o algoritmo vai usar.

- problema: ordenar um vetor
- instância: o vetor [3, 1, 2]

O algoritmo tem que funcionar pra toda instância, não só pra que eu testei.

## Algoritmo x programa x instância

| | O que é |
|---|---|
| Algoritmo | a ideia, a lógica dos passos (não depende de linguagem) |
| Programa | a ideia escrita numa linguagem (Python, Java...) |
| Instância | o dado de entrada |

Exemplo do exercício da professora:

| Item | Resposta |
|---|---|
| código Python da ordenação por inserção | programa |
| "compare os dois números e exiba o maior" | algoritmo |
| vetor [5, 3, 8, 1] | instância |
| implementação Java de Dijkstra | programa |

Meu jeito de lembrar: se está em alguma linguagem, é programa. Se é a
explicação da lógica, é algoritmo. Se é dado, é instância.

## Algoritmo correto

Correto é quando, pra **toda** entrada, ele **para** e dá a **resposta certa**.
São duas coisas juntas, então tem dois jeitos de estar errado:

**1. Não parar**

```
BuscaInfinita(A, n, x)
1    i <- 1
2    enquanto A[i] ≠ x faça
3        i <- i + 1
```

Se o x não estiver no vetor, o i nunca para de crescer. Ele nem olha o n.

**2. Parar com resposta errada**

```
EncontraMaior(A, n)
1    maior <- 0
2    para i de 1 até n faça
3        se A[i] > maior então
4            maior <- A[i]
5    retorne maior
```

Testei no meu código ([buscas.py](../codigo/buscas.py)) com [-5, -2, -8, -1]:
a versão errada deu **0**, que nem existe no vetor. A certa começa com
`maior <- A[1]` e deu **-1**.

O problema é começar com um valor inventado (o 0). Começar com o primeiro
elemento do vetor resolve.

## Modelo de computador

Nas contas a gente imagina um computador simples: um processador só e memória
RAM simples. Os computadores de hoje são mais complicados, mas assim dá pra
comparar algoritmos sem se perder.

## Onde eu me confundi

- Achei que correto era só "dar a resposta certa". Também tem que parar.
- Confundi problema com instância. O vetor não é o problema, é um caso dele.
- Troquei entrada com saída nas características (saída é que precisa de pelo
  menos uma).
