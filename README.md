# Computabilidade e Complexidade de Algoritmos

Minhas anotações e exercícios da disciplina de Computabilidade e Complexidade
de Algoritmos, com a Prof. Flávia Lopes. Engenharia de Software, UDF.

Vou anotando o que entendi de cada aula com as minhas palavras, resolvendo os
exercícios da apostila e testando os algoritmos em Python pra ver se as contas
batem.

## Anotações

| Aula | Assunto |
|---|---|
| [Aula 1](anotacoes/aula-01-o-que-e-algoritmo.md) | o que é algoritmo, as 5 características, instância, algoritmo correto |
| [Aula 2](anotacoes/aula-02-tempo-de-execucao.md) | tempo de execução, melhor, pior e caso médio |
| [Aula 3](anotacoes/aula-03-contando-passos.md) | tabela da professora, regra do laço, somatórias, T(n) e notação O |
| [Aula 4](anotacoes/aula-04-ordenacao.md) | ordenação por inserção, BubbleSort e MergeSort |
| [Aula 5](anotacoes/aula-05-buscas.md) | busca linear e busca binária |
| [Aula 6](anotacoes/aula-06-problemas-dificeis.md) | problemas NP-completos |

## Exercícios

- [Capítulo 1](exercicios/capitulo-1.md) - os 2 propostos, com gabarito
- [Capítulo 2](exercicios/capitulo-2.md) - os 4 resolvidos da apostila e os 4
  propostos (resolução minha)

## Código

| Arquivo | O que faz |
|---|---|
| [insercao.py](codigo/insercao.py) | ordenação por inserção contando cada linha |
| [bubble_sort.py](codigo/bubble_sort.py) | BubbleSort contando comparações e trocas |
| [merge_sort.py](codigo/merge_sort.py) | MergeSort e Intercala contando comparações |
| [buscas.py](codigo/buscas.py) | busca linear, binária e o EncontraMaior certo e errado |
| [exercicios_cap2.py](codigo/exercicios_cap2.py) | confere as tabelas dos exercícios propostos |

Pra rodar, é só entrar na pasta `codigo` e rodar o arquivo:

```bash
python insercao.py
```

## Organização

```
.
├── README.md
├── anotacoes/     uma anotação por aula
├── exercicios/    exercícios de cada capítulo
└── codigo/        os algoritmos em Python
```

## Como eu estudo

1. Leio a anotação da aula.
2. Tento fazer os exercícios sem olhar a resposta.
3. Rodo o código pra conferir os números.
4. Antes da prova leio as partes "Onde eu me confundi" de cada aula.
