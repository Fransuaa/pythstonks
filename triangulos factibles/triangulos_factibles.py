
print("-Crearemos un triangulo-")
a=float(input("Ingresa la longitud del lado 'A': "))
b=float(input("Ingresa la longitud del lado 'B': "))
c=float(input("Ingresa la longitud del lado 'C': "))

if a<(b+c) and b<(a+c) and c<(a+b):
    if(a==b==c):
        print("\n>> Con estas medidas se puede formar un triangulo equilatero.")       
    elif(a!=b!=c):
        print("\n>> Con estas medidas se puede formar un triangulo isoceles.")       
    else:
        print("\n>> Con estas medidas se puede formar un triangulo escaleno.")        
else:
    print("\n>> No se puede formar un triangulo con estas medidas!")

input()

