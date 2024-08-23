prodeletronic = []
while True:
    nome = input("digite o nome do produto: ")
    prodeletronic.append(nome)
    resp = input("deseja continuar [s][n]")
    if resp.upper() == "N":
        break
    print("Digite um produto eletronicos")
print(prodeletronic)
