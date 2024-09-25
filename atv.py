# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
aprovado = 0 
for i in range (5):
    nota = float(input("digite a nota do aluno"))
    if nota >= 7:
        aprovado += 1
        print("total de alunos aprovados:" , aprovado)