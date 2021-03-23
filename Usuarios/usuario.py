import datetime
import hashlib
import Usuarios.conexion as conex

connect = conex.conectar()
database = connect[0]
cursor = connect[1]

class usuario:

    #Constructor para recibir los datos que el usuario haya imgresado
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):

        #Importamos la fecha de hoy
        fecha = datetime.datetime.now()
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #En una variable, guardamos la accion de ingresar los datos
        sql = "INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"

        #En otra variable guardamos los datos del constructor, la contraseña cifrada y la fecha
        usu = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            #Realizamos la consulta con las dos variables
            cursor.execute(sql, usu)
            #Guardamos
            database.commit()
            #Mostrara 1 si el registro fue exitoso
            result = [cursor.rowcount, self]
        except:
            #Mostrara 0 si no fue exitoso
            result= [0, self]

        return result

    def identificar(self):
        #En una variable guardamos las instrucciones de la consulta
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        #Ciframos la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usu = (self.email, cifrado.hexdigest())

        #Realizamos la consulta
        cursor.execute(sql, usu)
        #Devolvemos los datos del usuario obtenidos de la consulta
        result = cursor.fetchone()

        return result