print('sorteio iniciado...')
import random
numeros = (1,10)
 #enquanto a lista não tiver vazia
while numeros:
     input(f"\nPressinone Enter para sortear o numero...")
    
     numero_sorteado = random.randint(1,10) #sorteia um nome da lista atual
     
     print(f"numero sorteado: {numero_sorteado}")
    

print('\nTodos os numeros foram sorteado.')