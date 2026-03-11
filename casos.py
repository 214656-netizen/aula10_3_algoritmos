#Escolha do usuário quanto ao atendimento de um curso de informática
opcao = int(input("Digite a opção que vocë deseja\n1 para falar com humano\n2 para falar com robo\n3 para duvidas frequentes\nOpção: "))
match opcao:
    case 1:
        print("Aguarde na lista de espera. Posição atual: 2")
    case 2:
        print("bip bop sou um robo xD")
    case 3:
        print("nao ha nenhuma duvida no nosso curso, de nada")
    case _:
        print("error")