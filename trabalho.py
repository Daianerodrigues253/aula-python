cadastro = []

for i in range(3):
    nome = input('Digite seu nome: ')
    filme = input('Digite o nome do filme: ')

    while True:
        try:
            nota = float(input('Digite a nota do filme (0 a 10): '))
            if 0 <= nota <= 10:
                break  # vai fechar o looping
            else:
                print('Nota inválida! Tente novamente.')
        except ValueError:
            print('Digite um número válido!')


    cadastro.append({
        'nome': nome,
        'filme': filme,
        'nota': nota
    })
    

print('\nCadastro finalizado:')
for item in cadastro:
    print(f"Nome: {item['nome']}, Filme: {item['filme']}, Nota: {item['nota']}")

