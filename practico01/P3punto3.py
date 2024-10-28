print("\n")
print ("#### Paso #3 - Sentencias de Control ####")
print("\n")
print ("3.- If-elif-else statements")

# ingreso calificacion
calificacion = int(input("Ingresa una calificacion del 0 al 100: "))

# Verificacion
if 0 <= calificacion < 20:
    letra = "A"
elif 20 <= calificacion < 40:
    letra = "B"
elif 40 <= calificacion < 60:
    letra = "C"
elif 60 <= calificacion < 80:
    letra = "D"
elif 80 <= calificacion <= 100:
    letra = "F"
else:
    letra = "Error" 
    print ("El valor ingresado no es valido") 

print("La calificacion alfabetica es:", letra)
print("\n")
