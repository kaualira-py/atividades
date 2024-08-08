p = int(input("Digite o valor do produto: "))
c1 = int(input("""
-------Código------
1.À VISTA (EM ESPECIE)
2.CARTÃO DE DÉBITO
3.CARTÃO DE CRÉDITO(VENCIMENTO)
-------------------------------
digite uma opção: """))

if c1==1:
    print("Seu desconto será de {}".format(p* 0.85))
elif c1==2:
    print("Seu desconto será de {}".format(p*0.9))
elif c1 ==3:
    print("Seu desconto será de {}".format(p*0.95))
else:
    print("Código inválido.")
