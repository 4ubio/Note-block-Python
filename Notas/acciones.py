import Notas.nota as model

class Acciones:

    def crear(self, usuario):
        print(f"¡Ok, {usuario[1]}! ¡Vamos a crear una nueva nota!")
        titulo = input("Introduce el titulo de tu nota: ")
        contenido = input("Introduce el contenido de tu nota: ")

        #Enviamos el id del usuario, titulo y contenido al constructor de la clase notas
        nota = model.notas(usuario[0], titulo, contenido)
        #Ejectutamos guardar en una variable
        guardar = nota.guardar()

        #Si se devuelve 1 se ha realizado con exito
        if guardar[0] >=1:
            print(f"\nPerfecto {usuario[1]}, has guardado tu nota: {nota.titulo}")
        #Si se devuelve 0 no se ha realizado con exito
        else:
            print("\nLo siento, no se ha guardado la nota")

    def mostrar(self, usuario):
        print(f"\nOk {usuario[1]}, estas son tus notas: \n")

        # Enviamos el id del usuario al constructor de la clase notas
        nota = model.notas(usuario[0])
        #En una variable llamamos a la funcion listar, guarda las notas en forma de tupla
        notas = nota.listar()

        for nota in notas:
            print("\n***********************************************")
            #Titulo de la nota
            print(nota[2])
            #Contenido de la nota
            print(nota[3])
            print("***********************************************\n")

    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}, vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a borrar: ")
        #Enviamos el ID del usuario y el titulo de la nota al constructor de la clase notas
        nota = model.notas(usuario[0], titulo)
        #Guardamos en una variable el llamar a la funcion eliminar y le pasamos el titulo
        eliminar = nota.eliminar(titulo)

        #Si la funcion devuelve 1 es exitosa
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota '{nota.titulo}' con exito")
        #Si la funcion devuelve 0 no fue exitosa
        else:
            print("No se ha borrado la nota")
