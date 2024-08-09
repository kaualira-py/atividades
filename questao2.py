u = (input("Usuário: "))
c = 3

for x in range(1,4):
    s = int(input("Digite sua semha: "))
    c -= 1
    if s==123456:
        print("Olá,{} seja bem vindo ao nosso banco.".format(u))
        break
    elif c ==2 or c ==1:
        print("senha incorreta, voce ainda tem {} chances".format(c))
    
    if c == 0:
        print("Sua senha foi bloqueada!, por favor, dirija-se a um de nossos caixas.")
        
