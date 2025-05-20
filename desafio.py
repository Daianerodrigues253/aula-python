def pagamento(horas, valor, dias):
    
    total = horas * valor * dias
    return total

def mostra_ajuda():
    
    print("\n--- Ajuda sobre o cálculo de pagamento ---")
    print("Este sistema calcula o pagamento total de um trabalhador com base:")
    print("- Horas trabalhadas por dia")
    print("- Valor recebido por hora")
    print("A fórmula utilizada é: horas * valor por hora * dias\n")

def main():
    while True:
        print("Menu:")
        print("1. Calcular pagamento")
        print("2. Ajuda")
        print("3. Sair")
        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == '1':
            try:
                horas = float(input("Informe o número de horas trabalhadas por dia: "))
                valor = float(input("Informe o valor recebido por hora: "))
                dias = int(input("Informe a quantidade de dias trabalhados: "))
                total = pagamento(horas, valor, dias)
                print(f"\nO total a pagar é: R$ {total:.2f}\n")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.\n")

        elif opcao == '2':
            mostra_ajuda()
        elif opcao == '3':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.\n")

if __name__ == "__main__":
    main()

