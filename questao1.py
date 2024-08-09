a = b = c = d = 0
mn = ''
nm = input("nome: ")
d = float(input("preçu: "))
c = d 
for x in range(1,5):
    nm = input("nome: ")
    d = float(input("preçu: "))
    a += d
    b += 1
    if d < c:
        d = c
        nm = mn
print(f"Média {a/b}, nome do menor{mn}, preço do menor{c}")
