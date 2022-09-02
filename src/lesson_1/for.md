O laço `for`
============

Outro caso muito comum em que precisamos executar um código repetidamente é
quando precisamos fazer isso um número específico de vezes, ou uma vez para
cada elemento em uma coleção de valores. Para estes casos, o laço `for` é o
mais indicado.

```python
{{#include for.py}}
```

Aqui temos um laço `for`, cuja estutura será sempre desta forma:

```python
{{#include for.py:5}}
```

O laço `for` introduz uma variável (no exemplo, `grade`) e opera sobre um
_iterável_, ou seja, algum conjunto de valores sobre os quais podemos _iterar_,
um por um. No exemplo, o iterável é a _lista_ `grades`, que por sua natureza nos
permite obter seus elementos na ordem em que estão.

O `for` termina quando o iterável sobre o qual está iterando se esgota, ou seja,
neste caso, no fim da lista `grades`.

Dentro do for, vemos a seguinte construção:

```python
{{#include for.py:6}}
```

Este operador, `+=`, serve como um "atalho" para a atribuição de uma soma. É
equivalente a

```python
total = total + grade
```

Já dentro da f-string no `print`, temos um uso da função `len`:

```python
{{#include for.py:8}}
```

Esta função nos permite obter o tamanho de uma coleção, como a lista `grades`,
que tem tamanho `len(grades) == 3` (o operador `==` denota comparação, em
contraste com o `=` que denota atribuição).


A função `range`
----------------

Um caso razoavelmente comum é precisarmos de uma sequência de números inteiros,
que ande por um certo intervalo, com um certo passo. Para isso, Python tem a
função `range`:

```python
n = int(input("Give me a number: "))

for i in range(n):
    print(i)
```

Por padrão, `range` se inicia em `0` e anda de 1 em 1. É possível alterar este
comportamento. Ao receber dois parâmetros:

```python
for i in range(3, 9):
    print(i)
```

o primeiro é o início e o segundo o final. Já ao receber três parâmetros, o terceiro
é o passo:

```python
for i in range(3, 18, 2):
    print(i)
```

O elemento final é sempre _exclusivo_, ou seja, não faz parte dos valores gerados.
O valor de início é _inclusivo_.

Lembre-se que para iterar sobre listas não é necessário o uso de `range` para indexar
os valores. Isso faz com que a necessidade do `range` seja razoavelmente limitada.
