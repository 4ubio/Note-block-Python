import Usuarios.conexion as conex

connect = conex.conectar()
database = connect[0]
cursor = connect[1]


class notas:

    #Guarda los datos en la clase, titulo y contenido no son obligatorios
    def __init__(self, usuario_id, titulo = "", contenido = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.contenido = contenido


    def guardar(self):
        #Guardamos las instrucciones en una variable
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        #Guardamos los datos en una variable
        nota = self.usuario_id, self.titulo, self.contenido
        #Realizamos la consulta
        cursor.execute(sql, nota)
        #Guardamos
        database.commit()

        #Devolvemos 1 si se ha hecho con exito o 0 si es incorrecto
        return [cursor.rowcount, self]

    def listar(self):
        #En una variable escribimos la consulta de las notas que tenga el ID del usuario ingresado
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        #Realizamos la consulta
        cursor.execute(sql)
        #En una variable guardamos_todo lo obtenido de la consulta
        result = cursor.fetchall()

        return result

    def eliminar(self, titulo):
        #En una variable guardamos la instruccion
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        #Ejectutamos la consulta
        cursor.execute(sql)
        #Guardamos
        database.commit()

        return [cursor.rowcount, self]