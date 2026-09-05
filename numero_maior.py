numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
#pede 2 números ao usuário.
if numero1 > numero2:
#compara os números e imprime o maior. (primeira condição else)
    print("O maior número é:", numero1)
elif numero2 > numero1:
#compara os números e imprime o maior. (segunda condição elif)
    print("O maior número é:", numero2)
else:
#ultima condição else, caso os números sejam iguais.
    print("Os números são iguais.")