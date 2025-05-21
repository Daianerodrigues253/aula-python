

cliente = []

for i in range(3):
    nome = input('Digite seu nome: ')
    filme = input('Digite o nome do filme: ')

    while True:
        
            nota = float(input('Digite a nota do filme (0 a 10): '))
            if 0 <= nota <= 10:
                break  
            else:
                print('Nota inválida! Tente novamente.')


    cliente.append({
        'nome': nome,
        'filme': filme,
        'nota': nota
    })
    

print('\nCadastro finalizado:')
for item in cliente:
    print(f"Nome: {item['nome']}, Filme: {item['filme']}, Nota: {item['nota']}")
