# /*
#  * Crea un programa que simule el comportamiento del sombrero selccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts:
#  *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
#  *   y crear el algoritmo seleccionador:
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  */

casas=["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]   
puntos=[0,0,0,0]


print("¡Bienvenido a Hogwarts!")
print("Soy el sombrero seleccionador y te realizaré algunas preguntas...\n")

print("¿Cómo te definirías?")
print("1. Valiente \n2. Ambicioso \n3. Leal  \n4. Ingenioso")
aux=int(input())
if aux==1:
    puntos[0]=+1
elif aux==2:
    puntos[1]=+1
elif aux==3:
    puntos[2]=+1
elif aux==4:
    puntos[3]=+1

print("\n¿Cuál es tu clase favorita?")
print("1. Sapo \n2. Lechuza \n3. Gato \n4. Serpiente")
aux=int(input())
if aux==1:
    puntos[0]=+1
elif aux==2:
    puntos[1]=+1
elif aux==3:
    puntos[2]=+1
elif aux==4:
    puntos[3]=+1

print("\n¿Dónde pasarías más tiempo?")
print("1. Sapo \n2. Lechuza \n3. Gato \n4. Serpiente")
aux=int(input())
if aux==1:
    puntos[0]=+1
elif aux==2:
    puntos[1]=+1
elif aux==3:
    puntos[2]=+1
elif aux==4:
    puntos[3]=+1

print("\n¿Cuál es tu mascota?")
print("1. Lechuza \n2. Serpiente \n3. Gato \n4. Sapo")
aux=int(input())
if aux==1:
    puntos[0]=+1
elif aux==2:
    puntos[1]=+1
elif aux==3:
    puntos[2]=+1
elif aux==4:
    puntos[3]=+1

print("\nY por ultimo... ¿En que casa crees que deberias estar?")
print("1. Gryffindor \n2. Slytherin \n3. Hufflepuff \n4. Ravenclaw")
aux=int(input())
if aux==1:
    puntos[0]=+2
elif aux==2:
    puntos[1]=+2
elif aux==3:
    puntos[2]=+2
elif aux==4:
    puntos[3]=+2




