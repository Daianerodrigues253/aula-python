import random 
nomes = ["camilla","daiane", "liz", "igor","kaique", "gustavo", "barbara"]
while nomes : #enquanto a lista não tiver vazia
    input(f"\nPressinone Enter para sortear o nome...")
    
    nome_sorteado = random.choice(nomes) #sorteia um nome da lista atual
    print(f"nome sorteado: {nome_sorteado}")
    
    nomes.remove(nome_sorteado) #remove o nome sorteado da lista

print('\nTodos os nomes foram sorteado.')