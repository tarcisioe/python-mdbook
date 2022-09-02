Um primeiro programa
====================

Agora que já conhecemos o interpretador e entendemos o básico de como iremos
interagir com a linguagem, vamos fazer um programa básico. Aqui está o código
completo:

```python
{{#include age.py}}
```

A primeira coisa a entendermos com este exemplo é o fluxo de execução de
Python: todo arquivo lido pelo interpretador será executado de cima a baixo,
linha por linha (veremos uma leve "exceção" a esta regra na aula 2). É
importante termos isto em mente sempre, pois será importante para nosso
entendimento de conceitos mais complexos ao longo do curso, como a ideia de
_modularização_, ou seja, organizar um programa em diversos arquivos.

Sabendo disso, podemos nós mesmos avaliar o programa linha por linha. As quatro
primeiras linhas são bastante semelhantes, pois desempenham todas o mesmo
papel: introduzem _variáveis_.


Variáveis
---------

Uma variável, em Python, pode ser resumida como um nome dado a um certo valor
que existe durante a execução do programa. Veremos que nem todos os valores com
os quais iremos operar ganharão um nome, mas neste programa, todos tem, ou
seja, todos os valores com os quais estamos trabalhando estão _atribuídos_ a
uma variável.

É possível imaginar a relação entre as variáveis e seus valores como uma
tabela. Dada a primeira linha do código, temos a tabela da seguinte forma:

```python
{{#include age.py:1}}
```

|  Nome  | Valor |
|--------|-------|
| `year` | 2022  |

E conforme as linhas seguintes executam, a tabela vai sendo atualizada:

```python
{{#include age.py:2:4}}
```

|  Nome        |    Valor   |
|--------------|------------|
| `year`       |      2022  |
| `age`        |        29  |
| `name`       | "Tarcísio" |
| `birth_year` |      1993  |


A função `print`
----------------

A última linha deste programa utiliza uma _função built-in_, ou seja, um código
pronto, já provido pela linguagem, sem necessidade de interferência nossa. Esta
função se chama `print` e serve para escrever ("imprimir") coisas. Neste caso,
estamos imprimindo na tela, que é o comportamento padrão da função:

```python
{{#include age.py:5}}
```

```
$ python -m age
Hello, Tarcísio. I see you were born in 1993!
```

Perceba que há uma diferença entre o texto utilizado na variável `name`
(`"Tarcísio"`) e o texto utilizado como parâmetro da função `print` (`f"Hello
{name} ..."`). Enquanto o primeiro é o que chamamos de um _valor literal de
string_, que é como chamamos a representação computacional de texto, o segundo
é uma _f-string_, ou _format string_. Notamos isto pela letra `f` antes de
abrir as aspas.

Em uma f-string, podemos acessar, dentro de chaves (`{}`) construções da
linguagem que nos entreguem valores que possam, por sua vez, serem
transformados em texto. Assim, facilita-se bastante a construção de strings com
base nos valores disponíveis no momento.

Poderíamos escrever a f-string da última linha da seguinte forma:

```python
print(f"Hello, {name}, I see you were born in {year - age}.")
```

Assim, a variável `birth_year` deixaria de ser necessária. Neste caso, o valor
produzido pela expressão `year - age` está sendo utilizado sem nunca ganhar um
nome, ou seja, sem nunca ser atribuído a uma variável. Assim, desenha-se uma
distinção clara: variáveis não _são_ valores e valores não _são_ variáveis.
Dizemos que variáveis, a qualquer momento de sua existência, _referem-se_ a um
valor. E, pelo lado inverso, um valor pode existir, brevemente,
independentemente de estar sendo referenciado por uma variável.

Estudaremos a criação de novas funções na aula 2.


O conceito de módulo
--------------------

Em Python, todo arquivo `.py` que tenha um nome de acordo com a convenção de
nomenclatura (letras, números e `_`, não podendo começar com um número) é um
_módulo_. Este conceito, em isolamento, não é estritamente útil, mas vale ser
mantido em mente para um melhor entendimento, mais adiante no curso, da forma
como organizamos código em Python em diferentes arquivos que conseguem
referenciar uns aos outros.

O comando `python -m` que já foi referenciado anteriormente, faz alusão a isso:
o parâmetro `-m` vem de `module` e "executa um módulo como um script". Veremos
eventualmente que executar os arquivos desta forma nos dará um comportamento
consistente e útil, quando estivermos trabalhando com mais arquivos.
