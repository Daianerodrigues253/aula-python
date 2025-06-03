#cadastro de produtos e estoque

nome_do_produto= ""
soma_produto = 0
quantidade_em_estoque= 0 
maior_quantidade=0

while True:
    nome = input("Digite o nome do produto: ")
    quantidade_str = int(input("Digite a quantidade em estoque: "))

    maior_quantidade += quantidade_str
    soma_produto += 1

    if nome_do_produto == 1 or soma_produto > maior_quantidade:
        maior_quantidade = nome_do_produto
        maior_quantidade = quantidade_em_estoque

    while True:
        resposta = input("Deseja continuar? (sim/nao): ").strip().lower()
        if resposta in ['sim', 'nao']:
            break
        else:
            print("Resposta inválida. Digite apenas 'sim' ou 'nao'.")

    if resposta == 'nao':
        break

# Calcular média de idade
    if soma_produto > 0:
      media_estoque =quantidade_em_estoque/ soma_produto
    else:
     print("Nenhum produto foi cadastrado.")



print(f"\nTotal de produtos cadastrados: {nome_do_produto}")
print(f"Soma total das quantidades em estoque: {soma_produto}")
print(f"Média de estoque por produto: {media_estoque:.2f}")
print(f"Produto com maior quantidade em estoque: {quantidade_em_estoque} ({maior_quantidade} unidades)")

