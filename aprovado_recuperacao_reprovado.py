nome = input("Digite o nome do aluno: ")
#entrada do nome do aluno.

nota1 = float(input("Digite a primeira nota: "))
#entrada da primeira nota.

nota2 = float(input("Digite a segunda nota: "))
#entrada da segunda nota.

nota3 = float(input("Digite a terceira nota: "))
#entrada da terceira nota.

media = (nota1 + nota2 + nota3) / 3
#calculo da média da nota do aluno.

if media >= 7:
    print(f"O aluno {nome} foi aprovado com média de: {media}")
#se a média for maior ou igual a 7, o aluno é aprovado!

elif media >= 5:
    print(f"O aluno {nome} está de recuperação com média de: {media}")
#se a média for maior ou igual a 5, o aluno está de recuperação!

else:
    print(f"O aluno {nome} foi reprovado com média de: {media}")
#se a média for menor que 5, o aluno é reprovado!