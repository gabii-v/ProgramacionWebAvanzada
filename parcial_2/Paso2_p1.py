print("\n")
print ("#### Paso #2 - Clases ####")
print("\n")
print (" 1.- Clase Persona: ")


# clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


persona1 = Persona("Juan", 25)
persona1.saludar() 
