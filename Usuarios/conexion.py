import mysql.connector

def conectar():
    #Creamos la base de datos
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
        port=3306
    )

    #Creamos el cursor
    cursor = database.cursor(buffered=True)

    return database, cursor