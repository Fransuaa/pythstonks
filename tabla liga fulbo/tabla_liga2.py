import os

def cargar_equipo():
    equipo=[]
    equipo.append(input("Nombre del equipo: "))
    return equipo

def calcular(pg,pe):
    pts=(pg*3)+pe
    return pts

equipos=[]
menu=0
liga=False
while menu!=4:
    n=len(equipos)

    os.system("cls")
    print("\n//- MENU -//")
    print("1. Cargar")
    print("2. Mostrar")
    print("3. Crear Torneo")
    print("4. Salir")

    menu=int(input("\nElige una de las opciones: "))

    # if menu.isdigit()==False:
    #     menu=6
    # else:
    #     menu=int(menu)

    if (menu>4 or menu<1):
        print("Ingresa una opcion valida...")

    elif menu==1 and liga==False:
        equipos.append(cargar_equipo())
        input("Carga Exitosa!")

    elif menu==1 and liga==True:
        input("No puedes cargar equipos mientras hay una liga en curso...")

    elif menu==2:
        for i in equipos:
            print(i)
        input()

    if menu==3:
        print("Tienes ",n," equipos cargados")
        
        
        x=input("¿Seguro deseas iniciar la liga? Ten en cuenta que no podras cargar nuevos equipos hasta que el torneo finalice (y/n)")
        if (x=="y"):
            liga=True
        else:
            print()