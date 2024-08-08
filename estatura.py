estat1=float(input("digite uma estatura: "))
estat2=float(input("digite ota estatura: "))
estat3=float(input("digite uma ota estatura: "))
if estat1==estat2 or estat1==estat3 or estat3==estat2:
    print("ha, pelo menos, duas estaturas iguais")
else:
    if estat3>estat2 and estat3>estat1:
        print("a terceira estatura é a maior".format(estat3))
    elif estat2>estat3 and estat2>estat1:
        print("a segunda estatura é a maior".format(estat2))
    elif estat1>estat2 and estat1>estat3:
        print("a primeira estatura é a maior".format(estat1))
      
