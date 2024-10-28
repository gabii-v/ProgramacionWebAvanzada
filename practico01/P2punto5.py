print("\n")
print ("#### Paso #2 - Tipos de datos ####")
print("\n")
print ("5.- Diccionarios")


mi_diccionario = {
    "nombre": "Gabriel",      
    "edad": 25,             
    "altura": 1.73          
}

print("Valor de la primera clave (nombre):", mi_diccionario["nombre"])

mi_diccionario["ciudad"] = "Viedma"
print("clave agregada (ciudad):", mi_diccionario["ciudad"])

print (mi_diccionario)
print("\n")

mi_diccionario["edad"] = 50

print ("segunda clave modificada:", mi_diccionario)
print("\n")