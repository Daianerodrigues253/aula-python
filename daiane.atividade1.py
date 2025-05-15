alunos = []

for i in range (5):
    nome=input("digite o nome do aluno: ")
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    media = (nota1 + nota2) /2
    status ="Aprovado" if media >= 6 else "Reprovado"

    alunos.append([nome, nota1, nota2, media, status])
print("\n---resultado final---")

for aluno in alunos : 
 print(f"{aluno[0]} - nota1: {aluno[1]} | nota2: {aluno[2]} | media: {aluno[3]:.2f} | status: {aluno[4]}")

