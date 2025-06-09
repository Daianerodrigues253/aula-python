#programa para gerenciar o cadastro de ccliente e os produtos comprados.
nome_do_cliente = ""
quantidade_produto = 0
valor_gasto = 0
total = 0
soma_quantidade = 0

while True:
     nome = input("digite o nome do cliente:")

     try:
      quantidade_produto =  int(input("digite a quantidade de produto:"))
      valor_gasto = float(input("digite o valor gasto:"))
      total = quantidade_produto * valor_gasto
      soma_quantidade += quantidade_produto
      print(f"o valor total gasto foi de R${total:.2f}")
      print(f"o total de produtos comprados foi de {soma_quantidade}")
     except ValueError:
      print("digite o valor corretamente")
      continue
     continuar = input("deseja continuar? (S/N):").strip().upper()
     if continuar != 'S':
         break


     