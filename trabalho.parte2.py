contador = []
print("numeros primos de 1 a 100:")

for num in range(1,101):
    if num > 1: 
        eh_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
                print(num)
            