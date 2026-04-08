"""
Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos
anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a
tabela a seguir: - Até 3 anos de empresa: aumento de 3% - entre 3 e 10 anos: aumento
de 12.5% - 10 anos ou mais: aumento de 20%
"""

nome = input("Qual o nome do funcionário?: ")
s = float(input("Qual o salário deste funcionario?: "))
anos = int(input("A quanto tempo este funcionário trabalha na empresa?: "))

if anos <= 3:
    print(
        f"O/A senhor(a) {nome} receberá um aumento de 3% que equivale a um salário de {s + (s * 0.03)}"
    )
elif 3 <= anos < 10:
    print(
        f"O/A senhor(a) {nome} receberá um aumento de 12.5% que equivale a um salário de {s + (s * 0.125)}"
    )
else:
    print(
        f"O/A senhor(a) {nome} receberá um aumento de 20% que equivale a um salário de {s + (s * 0.2)}"
    )
