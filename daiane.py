#cria uma lista vazia que ira armazenar os dados das comisso~es dos funcionarios 
comissoes = []
#loop que, neste caso, roda apenas 1 vez (poderia ser aumentado para mais funcionarios)
for i in range(1):
 nome = input("digite o nome do funcionario:")
comissaoum= float(input("digite a sua comissão no primeiro mês:"))
#float (numero com virgula)
comissaodois = float(input("digite a sua comissão no segundo mês:"))

#calcula a média 
media = (comissaoum + comissaodois) / 2 
#adiciona os dados coletados á lista 'comissoes'no formato de  dicionário
comissoes.append({
   "nome": nome,
   "comissão 1": comissaoum,
   "comissão 2": comissaodois,
   "média":media 
    })
print("\n---resultado final---")
#inicia um novo loop que percorre cada comissão da lista comissões
for comissao in comissoes:
    print(f"{comissao['nome']} - comissão 1: {comissao['comissão 1']}) | comissão 2:{comissao['comissão 2']} | média: {comissao['média']:.2f}")

