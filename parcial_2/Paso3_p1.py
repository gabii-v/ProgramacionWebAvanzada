print("\n")
print ("#### Paso #3 - Decorador ####")
print("\n")
print (" 1.- Decorador Simple para Mostrar Mensajes: ")


# decorador decorador_mensaje
def decorador_mensaje(func):
    def wrapper():
        print("Inicio de la función.")
        func()
        print("Fin de la función.")
    return wrapper

# funcion principal 
@decorador_mensaje
def funcion_principal():
    print("Esta es la función principal.")


funcion_principal() 




