import sqlite3 as sql


def createDB():
    connect=sql.connect("database/musica.db")
    connect.commit()
    connect.close()

def createTable():
    connect=sql.connect("database/musica.db")
    cursor=connect.cursor()

    cursor.execute(
        """CREATE TABLE artista( 
            nombre text,
            id integer
        ) """
    )

    connect.commit()
    connect.close()

def insertRow(nombre,id):
    connect=sql.connect("database/musica.db")
    cursor=connect.cursor()
    crud=f"INSERT INTO artista VALUES('{nombre}',{id})"
    cursor.execute(crud)
    connect.commit()
    connect.close()

def insertRows(artistas):
    connect=sql.connect("database/musica.db")
    cursor=connect.cursor()

    crud=f"INSERT INTO artista VALUES(?,?)"

    cursor.executemany(crud,artistas)
    connect.commit()
    connect.close()

def readRow():
    connect=sql.connect("database/musica.db")
    cursor=connect.cursor()
    crud=f"SELECT * FROM artista"
    cursor.execute(crud)
    datos=cursor.fetchall()
    connect.commit()
    connect.close()
    print(datos)


if __name__ == "__main__":
    artistas=[
        ("Fito Paez",1),
        ("Babasonicos",2),
        ("La Renga",3)
    ]
    
    #insertRows(artistas)

    readRow()



    
