
banco = ""
nome = ""
opçao = 0
while True:
        print("**MENU PRINCIPAL")
        print("1.cadastra o nome do banco")
        print("2.cadastra o nome do cliente")
        print("3.sair do sistema")
        print("****************")
        opçao=int(input("Escolha uma opção:"))
        if opçao == 1:
            banco=input("digite o nome do banco")
            print ("nome banco cadastrado")
        elif opçao ==2:
            nome=input("digite seu nome")
            print("nome cadastrado")
        
        elif opçao == 3:
            print("encerrando..." )
            break
        else:
            print("opção invalida")

