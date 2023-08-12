def calcular(pg,pe):
    pts=(pg*3)+pe
    return pts

def cargar_equipo():
    equipo=[]
    x=input("Nombre del equipo")
    equipo.append(x)
    return equipo


equipos=[["MUN"],
         ["FCB"],
         ["MIL"],
         ["INT"],
         ["RMA"],
         ["BVB"]]

y=0
for i in equipos:
    print(equipos[y][0])
    pj=(len(equipos)-1)
    equipos[y].append(pj)

    pg=int(input("partidos ganados? "))
    equipos[y].append(pg)
    pp=int(input("partidos perdidos? "))
    equipos[y].append(pp)
    pe=int(input("partidos empatados? "))
    equipos[y].append(pe)

    gf=int(input("goles a favor? "))
    equipos[y].append(gf)
    gc=int(input("goles en contra? "))
    equipos[y].append(gc)
    equipos[y].append(gf-gc)

    equipos[y].append(calcular(pg,pe))
    print("\n")
    y+=1
equipos=sorted(equipos, key=lambda x:(x[8],x[7],[5]), reverse=True)

print("Nombre|PJ |PG |PP |PE |GF |GC |DG | PTS")

for i in equipos:
    print(i[0],"  |",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"| ",i[8],)
    





# (Número de equipos * (Número de equipos - 1)) / 2 = N° TOTALES DE PARTIDO
# Número de equipos - 1 = N° DE PARTIDOS POR EQUIPO