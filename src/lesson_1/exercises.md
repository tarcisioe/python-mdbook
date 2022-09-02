Exercícios
==========


1. Escreva um laço que passe **por todos** os números de 1 a n,
   mas imprima apenas os pares. Peça n para o usuário. Dicas:
    - O operador `%` pode ser utilizado para obter o resto da divisão.
    - Lembre-se que a entrada do usuário virá como texto.

2. Faça um laço baseado no da questão anterior. Neste laço, para cada número,
   imprima:
    * `fizz` se o número for divisível por 3
    * `buzz` se o número for divisível por 5
    * `fizzbuzz` se o número for divisível por ambos
    * O próprio número, em todos os outros casos.
    * Lembre de **não** imprimir o número nos três primeiros casos.

3. Utilizando algum dos tipos de laço vistos nesta aula, imprima os valores da
   sequência de Fibonacci, das seguintes formas:
    * Dado um `n`, até o `n`-ésimo elemento da sequência.
    * Dado um `x`, até o último elemento da sequência que seja menor ou igual
      a `x`

    > **Sequência de fibonacci:** A sequência de números dada por `f(n) = f(n-1) + f(n-2)`, onde
        convenciona-se que `f(0) = 0` e `f(1) = 1`.
    >
    > Exemplo da sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

4. Utilizando algum dos tipos de laço vistos em aula, determine se um texto
   dado pelo usuário é ou não um palíndromo, escrevendo `palindrome` se for, ou
   `not a palindrome` se não for.

    > **Palíndromo**: Uma string que é igual a si mesma se lida de trás para
      frente, como `arara`.

    * Para acessar cada caractere da string, pode se usar `s[i]` para uma
      string `s` e uma posição `i`.
    * Lembre-se que as posições na string iniciam-se em 0.
