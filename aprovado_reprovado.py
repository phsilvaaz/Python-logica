nome = input("Digite o nome do aluno: ")
#entrada do nome do aluno.

nota1 = float(input("Digite a primeira nota: "))
#entrada da primeira nota.

nota2 = float(input("Digite a segunda nota: "))
#entrada da segunda nota.

media = (nota1 + nota2) / 2
#calculo da média da nota do aluno.

if media >= 6:
    print(f"O aluno {nome} foi aprovado com média de: {media}")
#se a média for maior ou igual a 6, o aluno é aprovado!

else:
    print(f"O aluno {nome} foi reprovado com média de: {media}")
#se a média for menor que 6, o aluno é reprovado!