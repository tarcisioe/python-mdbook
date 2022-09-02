Tipos built-in
==============

Até agora, trabalhamos com diversos valores que representavam coisas bastante
diferentes: valores numéricos inteiros, fracionários, textuais, coleções de
outros valores, etc. Agora passaremos algum tempo entendendo como Python
diferencia valores em _tipos_, dedicados, cada um, a representar um conjunto
diferente de objetos.


O que são tipos?
----------------

Um _tipo_ é um conjunto de valores específico e quais operações podem ser
feitas sobre eles. Python é uma linguagem _tipada_, ou seja, os valores
representáveis na linguagem são sempre de um _tipo_ e carregam consigo de
alguma forma informação sobre a qual tipo pertencem.

É possível verificar o tipo de um valor em tempo de execução, utilizando a
função `type`:

```
>>> type(2)
<class 'int'>
>>> type("abc")
<class 'str'>
>>> type(3.7)
<class 'float'>
>>> a = "Hi!"
>>> type(a)
<class 'str'>
```

Um _valor_ não pode mudar
de tipo durante a execução, mas uma _variável_ pode passar a referenciar um
valor de um tipo diferente do que referenciava anteriormente:

```python
a = 2
a = 4.7
a = "Hi!"
```

Apesar desta possibilidade existir, não é comum que isso seja necessário, salvo
casos muito pontuais. Ferramentas de análise estática não costumam permitir que
variáveis assumam outro tipo durante a execução, salvo isso ser requisitado
explicitamente pelo programador.

Veremos na aula 2 como introduzir tipos novos para permitir uma melhor
modelagem dos programas que pretendemos resolver. Aqui, veremos alguns dos
tipos que já existem na linguagem, ou _tipos built-in_.


O tipo `int`
------------

O primeiro tipo que vimos nesta aula representa números inteiros: o tipo `int`.

```python
a = 2  # type(a) == <class 'int'>
```

O tipo `int` representa qualquer número inteiro, com ou sem sinal, e não tem
limite inferior ou superior de representação:


```python
>>> from math import factorial
>>> factorial(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
```

Com o tipo `int` podemos fazer as operações básicas com números inteiros:

```
>>> 2 + 4
6
>>> 2 - 4
-2
>>> 2 * 4
8
>>> 2 / 4
0.5
>>> 2 // 4
0
>>> 2 ** 4
16
```

É importante notar que a divisão (`/`) resulta em um número fracionário, ou
seja, o resultado não é um novo inteiro. Para restringir o resultado aos
inteiros, obtendo apenas a parte inteira da divisão, utilize o operador de
divisão inteira (`//`). O operador de potenciação é `**`, ou seja, `2**4` = 2⁴.


O tipo `float`
--------------


O tipo `bool`
--------------


O tipo `str`
--------------


O tipo `list`
--------------


O tipo `dict`
--------------


O tipo `set`
--------------
