print("\n")
print ("#### Paso #2 - Clases ####")
print("\n")
print (" 2.- Clase Rectangulo: ")


# clase Rectangulo
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # metodo para calcular el area
    def area(self):
        return self.ancho * self.alto

    # metodo para calcular el perimetro
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

rectangulo1 = Rectangulo(4, 7)
print("El area del rectangulo es: ", rectangulo1.area())  
print("El perimetro del rectangulo es: ", rectangulo1.perimetro())  
