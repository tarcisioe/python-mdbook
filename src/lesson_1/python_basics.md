Como utilizamos Python?
=======================

Iniciaremos nosso curso com uma breve apresentação da linguagem Python: como
ela funciona e quais suas aplicações mais comuns.


O interpretador
---------------

Na contramão de algumas linguagens como C, C++ ou Rust, que são _compiladas_ a
fim de gerar um _executável nativo_, Python, em suas implementações mais
comuns, costuma seguir um modelo de execução _interpretada_.

Uma execução interpretada implica que, para executar os programas que
escrevemos, um outro programa (o _interpretador_) estará sempre responsável por
ler nosso código fonte e executá-lo.

Isto tem três implicações dignas de nota:
- Permite, com facilidade, um nível de abstração bastante alto.
- Facilita o ciclo de desenvolvimento (programar <-> executar), pois não há
  passo intermediário.
- Causa, obrigatoriamente, certo custo "extra" de execução: o código em geral
  será pouco otimizado e há uma camada extra entre o programa e o _hardware_.

Veremos então bem frequentemente o seguinte estilo de comando sendo executado:

```
$ python main.py
Hello, world!
```

ou, idealmente:

```
$ python -m main
Hello, world!
```

(veremos a diferença destes comandos ao longo do curso).


Tipagem dinâmica, erros durante a execução
------------------------------------------

Como não há um passo intermediário obrigatório entre programar e executar o
programa, não há distinção entre o passo de validação do programa (geralmente
chamado _análise estática_) e a execução. Portanto, quando cometemos erros
ao programar, eles são descobertos, mais cedo ou mais tarde, durante a execução
do programa (também chamada _runtime_).

Veja o resultado da execução do seguinte programa:

```python
{{#include print_with_type_error.py}}
```

```
$ python -m print_with_type_error
Vamos tentar somar um número com um texto!
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/tarcisioe/teaching/soberana/python/python-mdbook/src/lesson_1/print_with_type_error.py", line 2, in <module>
    print(2 + "a")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Como podemos perceber, a primeira linha do programa executou sem problemas,
enquanto a segunda causou um erro. Em geral, como programadores, consideraremos
erros em tempo de execução como ocorrendo _tarde demais_, portanto veremos
ao longo do curso ferramentas que nos ajudarão a encontrar boa parte dos erros
antes de executar o programa.


O interpretador é interativo
----------------------------

O interpretador de Python, por sua natureza, permite facilmente que façamos
testes com a linguagem interativamente. Se executarmos somente `python`, entramos
em uma sessão interativa do interpretador:

```
$ python
Python 3.10.5 (main, Aug  1 2022, 07:53:20) [GCC 12.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> print("Hello!!!")
Hello!!!
>>> a = 4
>>> print(a + 3)
7
```

Isto nos abre possibilidades de testes e experimentos muito simples e rápidos
com a linguagem (além de fornecer uma ótima calculadora!).
