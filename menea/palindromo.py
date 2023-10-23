def es_palindromo(palabra):
    aux=palabra.lower().replace(" ", "")
    return aux==aux[::-1]

while True:    
    palabra = input("# Ingrese una palabra: ")
    
    if palabra=="exit()":
        break
    elif es_palindromo(palabra):
        print(f"'{palabra}' es un palíndromo. \n")
    else:
        print(f"'{palabra}' no es un palíndromo. \n")

