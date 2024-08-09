soma = 0
medicamento = input("Medicamento: ")
preco       = float(input("R$: "))
mais_barato = medicamento
menor_preco = preco
soma += preco

for x in range(4):
   medicamento = input("Medicamento: ")
   preco       = float(input("R$: "))
   if preco < menor_preco:
      menor_preco = preco
      mais_barato = medicamento
   soma += preco

media = soma / 5
print(f"{mais_barato} é o medicamento mais barato e custa R$ {menor_preco:.2f}.")
print(f"Média dos preços: R$ {media:.2f}.")
