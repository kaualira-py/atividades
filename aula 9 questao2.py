a = int(input("Primeiro termo: "))
b = int(input("Quantidade de termos: "))
c = int(input("Razão: "))
f=0
for x in range(a,b+1,c):
    f += x
print(f)
