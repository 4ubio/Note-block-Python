import Usuarios.usuario as model
import Notas.acciones

class Acciones:

    def registros(self):
        print("\n¡Ok! Vamos a registrarte en el sistema")
        nombre = input("¿Cual es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        email = input("¿Cual es tu email? ")
        password = input("¿Cual es tu contraseña? ")

        #Enviamos los parametros ingresados por el usuario en una variable al constructor de la clase usuario
        usuario = model.usuario(nombre, apellidos, email, password)
        #Una vez ingresados, llamamos a la funcion registrar
        registro = usuario.registrar()

        #Si la funcion registrar fue correcta devolvera 1 y mostrara que el registro ha sido exitoso
        if registro[0] >= 1:
            print(f"Perfecto {nombre} {apellidos}. Te has registrado con el email {email}")
        # Si la funcion registrar fue incorrecta devolvera 0 y mostrara que el registro ha sido fallido
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("\n¡Ok! Ingresa tus datos")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            #en una variable, envia los datos al constructor de la clase usuario (el nombre y apellidos en blanco)
            usuario = model.usuario('','', email, password)
            #Llamamos a la funcion identificar y lo guardamos en una variable
            login = usuario.identificar()

            #Si el dato 3 de la base de datos en la tupla (email registrado) es igual al ingresado
            if email == login[3]:
                print(f"Bienvenido {login[1]} {login[2]}, te has registrado el {login[5]}")
                #La ejecucion del programa continuara con otra funcion y enviara la tupla del login
                self.proximasAcciones(login)

        except Exception as e:
            print("Login incorrecto, intenta mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
         
        - Crear nota (crear)
        - Mostrar notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer? ")
        #Llamamos a la clase Acciones del modulo acciones
        hazEL = Notas.acciones.Acciones()

        #Si la accion es crear, llamamos a la funcion crear y enviamos los datos del usuario (login)
        #Y despues continuamos con la ejecucion normal
        if accion == "crear":
            hazEL.crear(usuario)
            self.proximasAcciones(usuario)
        # Si la accion es mostrar, llamamos a la funcion mostrar y enviamos los datos del usuario (login)
        #Y despues continuamos con la ejecucion normal
        elif accion == "mostrar":
            hazEL.mostrar(usuario)
            self.proximasAcciones(usuario)

        # Si la accion es eliminar, llamamos a la funcion eliminar y enviamos los datos del usuario (login)
        #Y despues continuamos con la ejecucion normal
        elif accion == "eliminar":
            hazEL.borrar(usuario)
            self.proximasAcciones(usuario)

        # Si la accion es salir, el programa se cierra
        elif accion == "salir":
            print(f"Hasta pronto, {usuario[1]}")
            exit()

        # Si se ingresa cualquier otro comando, volvera a la ejecucion de acciones
        else:
            print("Ingresa un comando valido")
            self.proximasAcciones(usuario)
