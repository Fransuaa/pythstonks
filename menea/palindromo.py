def es_palindromo(palabra):
    aux=palabra.lower().replace(" ", "")
    return aux==aux[::-1]

xp=(True)
while xp==True:    
    palabra = input("# Ingrese una palabra: ")
    
    if palabra=="exit()":
        xp=False
    elif es_palindromo(palabra):
        print(f"'{palabra}' es un palíndromo. \n")
    else:
        print(f"'{palabra}' no es un palíndromo. \n")

