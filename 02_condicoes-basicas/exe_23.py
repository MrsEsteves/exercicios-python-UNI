"""
Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para
todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o
valor das compras do cliente e calcule o preço com desconto. Sabendo que: - Homens
ganham 5% de desconto - Mulheres ganham 13% de desconto
"""

nome = input("Qual o nome do cliente?: ")
sexo = input("Qual o sexo do cliente? (M/F): ").upper()
v_compras = float(input("Qual o valos das compras do cliente?: "))

if sexo == "M":
    print(
        f"Senhor {nome}, o seu desconto é de 5%, o valor a pagar é {v_compras - (v_compras * 0.05):g}."
    )
elif sexo == "F":
    print(
        f"Senhora {nome}, o seu desconto é de 13%, o valor a pagar é {v_compras - (v_compras * 0.13):g}."
    )
else:
    print("Opção inválida.")
