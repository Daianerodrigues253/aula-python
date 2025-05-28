def obter_qtd_doacao():
    while True:
        try:
            qtd = int(input("Digite a quantidade de quilos que deseja doar (de 1kg ou mais): "))
            if qtd >= 1:
                return qtd
            else:
                print("Por favor, insira um número inteiro maior ou igual a 1.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

def calcular_pacotes(qtd):
    pacotes_5kg = qtd // 5
    resto = qtd % 5

    pacotes_2kg = resto // 2
    resto = resto % 2

    pacotes_1kg = resto

    return pacotes_5kg, pacotes_2kg, pacotes_1kg

def main():
    print("Bem-vindo ao sistema de doação de alimentos!")
    qtd_doacao = obter_qtd_doacao()

    p5, p2, p1 = calcular_pacotes(qtd_doacao)

    print("\nSua doação será embalada da seguinte forma:")
    print(f"Pacotes de 5kg: {p5}")
    print(f"Pacotes de 2kg: {p2}")
    print(f"Pacotes de 1kg: {p1}")

    print("\nMuito obrigado pela sua doação!")

if __name__ == "__main__":
    main()