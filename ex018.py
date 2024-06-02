import math
an=float(input("Digite o ângulo desejado para saber qual é o seu seno e o seu cosseno"))
seno=math.sin(math.radians(an))
cosseno=math.cos(math.radians(an))
tangente=math.tan(math.radians(an))
print("O valor do ângulo digitado foi de {:.2f}, sendo asssim, seu seno vale {:.2f}, seu cosseno vale {:.2f} e sua tangente vale{:.2f}".format(an,seno,cosseno,tangente))
