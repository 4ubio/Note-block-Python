from Usuarios import acciones

#Asistente de ingreso al sistema
print("""
Acciones disponibles:
    -login
    -registro
""")

#Importamos la clase acciones en una variable
hazEL = acciones.Acciones()
accion = input("¿Qué quieres hacer? ")

#llamamos a la accion registro de la clase Acciones
if accion == "registro":
    hazEL.registros()

#llamamos a la accion login de la clase Acciones
elif accion == "login":
    hazEL.login()
