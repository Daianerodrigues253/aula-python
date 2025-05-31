print("cadastro de cidades")

nome_cidade = ""
populaçao_estimada = 0
soma = 0
total = 0

while True:
    nome = input("digite o nome da cidade:")
    populaçao = input("digite o numero da populaçao:")
  
    if populaçao .isdigit():
        populaçao = int(populaçao)
  
    else:
     print("populaçao invalida.digite apenas numeros.")
     continue
  
     
    
    total +=1
    soma += populaçao_estimada
 
    if populaçao > populaçao_estimada:
        populaçao_estimada = populaçao
        nome_cidade = nome
    
    continuar = input("deseja continuar? (S/N):").strip().upper()
    if continuar !='S':
        break

print("\n resultado final:")
print(f"total de cidades cadastradas: {total}")
print(f"media da populaçao entre todas as cidades{soma/total:.1f}populaçao")
print(f"nome da cidade mais populosa e sua respectiva populaçao:{populaçao_estimada}({nome_cidade}) populaçao")