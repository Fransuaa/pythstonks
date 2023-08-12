import random

# Definir los equipos de la liga
equipos = ['Equipo A', 'Equipo B', 'Equipo C', 'Equipo D']

# Crear una lista para almacenar los resultados de los partidos
resultados = []

# Función para simular un partido y actualizar los resultados
def simular_partido(local, visitante):
    # Simular el resultado del partido (0 = empate, 1 = local gana, 2 = visitante gana)
    resultado = random.randint(0, 2)
    
    # Actualizar los resultados del local
    if resultado == 0:
        local[2] += 1  # Empate
        local[3] += 1  # Partido jugado
        local[4] += 1  # Punto obtenido
    elif resultado == 1:
        local[1] += 1  # Victoria
        local[3] += 1  # Partido jugado
        local[4] += 3  # 3 puntos por victoria
    else:
        local[0] += 1  # Derrota
        local[3] += 1  # Partido jugado
    
    # Actualizar los resultados del visitante
    if resultado == 0:
        visitante[2] += 1
        visitante[3] += 1
        visitante[4] += 1
    elif resultado == 1:
        visitante[0] += 1
        visitante[3] += 1
    else:
        visitante[1] += 1
        visitante[3] += 1
        visitante[4] += 3

    # Agregar el resultado a la lista de resultados
    resultados.append((local[0], local[1], local[2], visitante[0], visitante[1], visitante[2]))

# Generar los partidos por fecha
def generar_partidos_por_fecha(equipos):
    partidos = []
    for i in range(len(equipos)-1):
        for j in range(i+1, len(equipos)):
            partidos.append((equipos[i], equipos[j]))
    random.shuffle(partidos)
    return partidos

# Simular todos los partidos y actualizar los resultados
def simular_liga(equipos):
    partidos_por_fecha = generar_partidos_por_fecha(equipos)
    for partido in partidos_por_fecha:
        simular_partido(partido[0], partido[1])

# Mostrar los resultados de la liga
def mostrar_resultados(equipos):
    print("Resultados de la liga:")
    print("{:<10s} {:>8s} {:>8s} {:>8s} {:>10s}".format("Equipo", "PG", "PE", "PP", "Puntos"))
    for equipo in equipos:
        print("{:<10s} {:>8d} {:>8d} {:>8d} {:>10d}".format(equipo[0], equipo[1], equipo[2], equipo[3], equipo[4]))

# Inicializar las listas de resultados para cada equipo
tabla_equipos = []
for equipo in equipos:
    tabla_equipos.append([0, 0, 0, 0, 0])  # [PG, PE, PP, Partidos jugados, Puntos]

# Simular la liga
simular_liga(tabla_equipos)

# Mostrar los resultados
mostrar_resultados(tabla_equipos)