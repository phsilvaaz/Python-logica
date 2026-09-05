#o código abaixo pede um número ao usuário.
numero = int(input("Digite um número: "))
#o código verifica se o número é par ou ímpar.
if numero % 2 == 0:
#o símbolo de "%" verifica se o número é ímpar ou par. Por conta que, o símbolo de "%" é o operador de módulo, que retorna o resto da divisão do número por 2. Se o resto for igual a 0, significa que o número é par, caso ao contrário, o número é ímpar.
    print("O número é par!")
else:
    print("O número é ímpar!")

#número % 6
#resto da divisão -> resto == 0 -> par
#resto != 0 -> ímpar
