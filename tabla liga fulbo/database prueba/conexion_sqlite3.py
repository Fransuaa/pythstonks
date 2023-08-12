import sqlite3 as sql

# CREAR DATABASE
def createDB(): 
    connect=sql.connect("database/equiposarg.db")
    connect.commit()
    connect.close()

# CREAR TABLA
def createTable(): 
    connect=sql.connect("database/equiposarg.db")
    cursor=connect.cursor()
    cursor.execute(
        """CREATE TABLE equipos(
            id integer,
            nombre text,
            creacion integer,
            titulos_nacionales integer,
            titulos_internacionales integer
        )"""
    )
    connect.commit()
    connect.close()

# INSERTAR REGISTRO EN DETERMINADA TABLA, EN ESTE CASO 'EQUIPOS'
def insertRow(id,nombre,creacion,tnac,tint): 
    connect=sql.connect("database/equiposarg.db")
    cursor=connect.cursor()

    instruccion=f"INSERT INTO equipos VALUES ({id},'{nombre}',{creacion},{tnac},{tint})"
    cursor.execute(instruccion)

    connect.commit()
    connect.close()

# DEVUELVE TODOS LOS DATOS DE UNA TABLA EN FORMA DE UNA LISTA DE TUPLAS
def readRow():
    connect=sql.connect("database/equiposarg.db")
    cursor=connect.cursor()

    instruccion=f"SELECT * FROM equipos" 
    cursor.execute(instruccion)
    datos=cursor.fetchall()      # 'fetchall' devuelve una lista de tuplas, que en este caso se almacena en <datos>

    connect.commit()
    connect.close()
    print(datos)  # imprime lista

# DEVUELVE TODOS LOS DATOS DE UNA TABLA ORDENADOS DE ACUERDO A UN CAMPO, DE MAYOR A MENOR O VICEVERSA, SEGUN SE INDIQUE
def readOrdered(field,a):
    connect=sql.connect("database/equiposarg.db")
    cursor=connect.cursor()

    instruccion=f"SELECT * FROM equipos ORDER BY {field} {a}"  # Devuelve los datos ordenados de acuerdo a {field} --> (campo especificado), en {a} se indica el orden (ASC o DESC)
    cursor.execute(instruccion)
    datos=cursor.fetchall()      

    connect.commit()
    connect.close()
    print(datos)  

def search():
    connect=sql.connect("database/equiposarg.db")
    cursor=connect.cursor()

    instruccion=f"SELECT * FROM equipos WHERE titulos_internacionales>=10 "  # Devuelve todos los registros donde <titulos_internacionales> sea igual o mayor a 10 
    cursor.execute(instruccion)
    datos=cursor.fetchall()      

    connect.commit()
    connect.close()
    print(datos)  

def update():
    connect=sql.connect("database/equiposarg.db")
    cursor=connect.cursor()

    instruccion=f"UPDATE equipos SET titulos_internacionales=55 WHERE nombre like 'ate%'"  # Devuelve todos los registros donde <titulos_internacionales> sea igual o mayor a 10 
    cursor.execute(instruccion)
  

    connect.commit()
    connect.close()
     




if __name__ == "__main__":
    # createDB()
    # createTable()
    # insertRow(2,"Boca Juniors",1905,52,22)
    # insertRow(3,"River Plate",1908,51,18)
    # insertRow(4,"Estudiantes LP",1905,8,6)
    # insertRow(5,"Atenas RC",1916,0,0)
    # readRow()
    # readOrdered("creacion","asc")
    # readOrdered("creacion","desc")
    # search()
    update()


