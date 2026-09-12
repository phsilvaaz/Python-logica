idade = int(input("Digite sua idade: "))
#int (INTEIRO) por conta que o código pede um número inteiro, input pede para o usuário digitar. Input é a entrada e recebimento.

if idade >= 18:
    print("Você pode adentrar à festa!")
#primeira condição, se tiver 18 anos ou mais pode entrar na festa!

elif idade >= 16:
    responsavel = input("Tem responsavél? ")
    if responsavel.lower == "Sim":  
        print("Pode entrar!")
    else: 
        print("Não poderá entrar!")
#condição com if e else dentro do elif (senão/se). se (if) tiver responsavél "sim" o sujeito pode adentrar a festa com responsanvél. senão (else) não poderá adentrar a festa.