A construção `if/elif/else`
==============================

Até agora, vimos código que segue um fluxo linear. Porém, logo vemos que isto
não é suficiente para escrever programas gerais: teremos, eventualmente, de
tomar decisões.

Para alterar o fluxo da execução do programa, temos as _estruturas de controle
de fluxo_. A primeira que veremos é a construção `if`/`elif`/`else`:

```python
{{#include if.py}}
```

Vamos focar primeiro na linha da expressão `if`:

```py
{{#include if.py:3}}
```

Primeiramente, vamos entender o conceito de _palavra-chave_ (ou _keyword_). A
palavra `if`, em Python, é uma palavra-chave, pois serve para iniciar um
condicional. Isto significa também que ela não pode ser utilizada em outros
contextos, nem como nome de variável:

```
>>> if = 3
  File "<stdin>", line 1
    if = 3
       ^
SyntaxError: invalid syntax
```

Após a palavra chave `if`, a linguagem espera que esteja descrita uma
_condição_. Esta condição é o que definirá se o código dentro do `if` irá ou
não executar, baseado em seu _valor verdade_. A operação `<` entre dois números
irá nos dar um valor do tipo `bool`, que pode ser `True` (verdadeiro) ou
`False` (falso):

```
>>> 4 < 5.75
True
>>> 6 < 5.75
False
```

Após a condição, temos o caractere `:`, que indica à linguagem que estamos
prestes a iniciar um _bloco_. Um bloco é um trecho de código que está subordinado
a alguma coisa: neste caso, subordinado ao condicional `if`:

```py
{{#include if.py:4}}
```

Em Python, um bloco é dado pela _indentação_, ou seja, o espaço em branco presente
no início da linha. Linhas sequenciais com a mesma indentação pertencem ao mesmo bloco.
Uma linha não-vazia que retorne à uma indentação anterior finaliza o bloco, como é a
linha do `elif`:

```py
{{#include if.py:5:6}}
```

**Nota:** Em Python, convenciona-se fazer a indentação de 4 em 4 espaços.
Qualquer bom editor de texto permite fazer a tecla `Tab` inserir 4 espaços ao
ser pressionada.

O `elif` funciona de maneira semelhante ao if. A diferença principal é que ele:

- Obrigatoriamente precisa vir após um `if`.
- É _mutuamente exclusivo_ à condição do `if`. Ou seja, **ainda que a condição
  do `else if` seja verdadeira**, se o bloco `if` executou, o `elif` não irá
  executar.

Por fim, temos o bloco `else`:

```py
{{#include if.py:7:8}}
```

O bloco `else` executa caso nenhum dos blocos `if` ou `elif` anteriores execute.
No caso, ele irá executar caso `grade` tenha um valor maior ou igual a `8.0`.

Na seção seguinte, veremos uma construção semelhante ao `if`, mas que permite
_repetir operações_: a construção `while`.


A função `input`
----------------

Na primeira linha do exemplo, temos o seguinte trecho:

```py
{{#include if.py:1}}
```

Aqui, estamos utilizando a função `input` para pedir ao usuário que entre uma
informação no terminal (mais precisamente, na _entrada padrão_). O argumento
da função `input` é o seu _prompt_, ou seja, o que deve ser mostrado ao usuário
antes de aguardar uma entrada.

O resultado da função `input` é sempre um texto, então utilizamos a função `float`
para convertê-lo para um valor numérico capaz de representar números fracionários.
Esta operação pode falhar, caso a entrada não seja um número válido. Experimente!
