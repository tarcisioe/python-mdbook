O laço `while`
==============

É muito comum, ao programar, ser necessário repetir alguma operação diversas
vezes, até alcançar alguma condição. Para isso utilizaremos _laços_. Veremos 2
tipos de laços. O primeiro é o laço `while`. O código nesse laço irá rodar
enquanto uma dada condição for verdadeira. Veja o código a seguir:

```python
{{#include while.py}}
```

Vamos analisar o `while` parte a parte:

```python
{{#include while.py:6}}
```

A condição do `while` é dada de forma semelhante ao `if`. Ela deve ser um valor
do tipo `bool` (`True` ou `False`). O corpo do laço executará repetidas vezes,
até que, **ao final** de uma das execuções, a condição deixe de ser verdadeira.

O código acima calcula, de forma numérica, a raiz quadrada de um número
qualquer `x`. Isso é feito utilizando o método de Newton.

O método de Newton se baseia em um chute inicial. Esse chute pode ser maior,
menor ou igual ao valor da raiz quadrada.

Após fazer um chute inicial (no nosso caso, arbitrariamente fixado em `1.0`), é
feita a média do valor chutado com `x` dividido pelo chute, nas linha a seguir:

```python
{{#include while.py:8}}
```

Vamos acompanhar as possibilidades:

Se o chute for muito abaixo da resposta real, `x/guess` será muito acima da
resposta real (pois a raiz quadrada é o número que, ao dividir `x`, resulta
nele mesmo), e a média entre os dois se aproximará da resposta. Por exemplo:

* Seja `x = 36`.
* Seja `guess = 3` (abaixo do valor correto, `6`).
* `x/guess == 12`, ou seja, acima do valor correto.
* A média entre `guess` e `x/guess` será `7.5`, aproximando-se da resposta
  correta.

O exato oposto também pode acontecer: se `x` for maior que a resposta correta,
`x/guess` será menor que a resposta e a média se aproximará do valor procurado.

* Seja `x = 36`.
* Seja `guess = 15` (acima do valor correto, `6`).
* `x/guess == 2.4`, ou seja, abaixo do valor correto.
* A média entre `guess` e `x/guess` será `8.7`, também aproximando-se da
  resposta correta.

O resultado será usado como um novo chute, e o chute anterior é registrado na
variável `old`.

Perceba a condição do while: ele se quebra quando o chute anterior for igual ao
novo chute. Isso ocorrerá quando a resposta for a correta, pois `guess` será a
raiz quadrada de `x`, logo `x/guess` será igual a `guess`, e também à média.

No geral, o laço while é uma forma ideal de representarmos a repetição de
operações quando não sabemos o número necessário de repetições, e sim uma
condição de parada. Quando sabemos quantos passos daremos, ou melhor, quando
temos uma _coleção de valores_ sobre os quais queremos computar algo,
utilizaremos o laço `for`, que veremos a seguir.
