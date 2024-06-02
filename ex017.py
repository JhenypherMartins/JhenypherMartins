co=float(input("Qual a medida do cateto oposto em centímetros?"))
ca=float(input("Qual a medida do cateto adjacente em centímetros?"))
h=(co**2+ca**2)**(1/2)
print("Desta forma, a hipotenusa mede {:.2f}cm".format(h))
