
banco=""
nome=""
conta=""
opçao=0
while True:
    print("MENU PRINCIPAL")
    print("1.cadastra nome do banco seu nome tipo de conta")
    print("2.ver dados cadastrados")
    print("3.sair do sistema")
    print("****************")
    opçao=int(input("escolha uma opçao:"))
    if opçao ==1:
       banco=input("digite o nome do banco")
       nome=input("digite seu nome")
       conta=input("digite o tipo de conta")
       print("dados cadastrados com sucesso")
    elif opçao ==2:
     
        print("nenhum dados cadastrados.")
    else:
        print("dados cadastrados com sucesso.")
        print(f"banco:{banco}")
        print(f"nome:{nome}")
        print(f"conta:{conta}")
    if opçao==3:
       print("encerrando o sistema...")
        
else:
        print("dados cadastrados com sucesso!")