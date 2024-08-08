from math import sqrt 
a = float(input("Digite um numero: "))
b = float(input("Digite um segundo numero: "))
c = float(input("Digite um terceiro numero: "))
delta=b*b -4*a*c
if delta == 0:
    x = -b / (2*a)
elif delta > 0:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print("""x1 = {}
x2 = {}""".format(x1,x2))
else:
    print("Não existe raiz real")
