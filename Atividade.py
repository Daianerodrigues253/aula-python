def main():
    nome = ""
    idade = 0
    opcao = 0
    while True:
        print("===MENU PRINCIPAL===")
        print("1. Cadastrar Novo Usuário")
        print("2. Ver Usuário Cadastrado")
        print("3. Sair do Sistema")
        print("*****************************")
        opcao=int(input("Escolha uma opacao"))
        if opcao ==1:
            nome=input("Digite seu nome: ")
            idade=int(input("Digite sua idade: "))
        elif opcao==2:
            if nome =="" or idade == 0:
                print("Nenhum dado Cadastrado.")
            else:
                print("Dados cadastrados com sucesso.")
                print("f:Nome: {nome}")
                print("f:Idade: {idade}")

        elif opcao ==3:
            print("Encerrando o Sistema...")
        break
    else:
        print("Opcao Inválida")

if __name__=="__main__":
    main()

                      