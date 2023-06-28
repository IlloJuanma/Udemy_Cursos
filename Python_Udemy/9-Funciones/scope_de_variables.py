# Una variable declarada dentro de una funcion se conoce como variable local, el ambito de la variable
# Una variable declarada fuera de una funcion se conoce como una variable global

mensaje1 = "Soy una variable global"

def MiFuncion():
    print("--- Estoy dentro de mi funcion ---")
    # Crear una variable local
    mensaje2 = "Soy una variable local"

    # Acceso a variable local
    print(mensaje2)

    # Acceso a variable global
    print(mensaje1)

# Llamar a mi funcion:
MiFuncion()

# Hacer cosas fuera de mi funcion:
print("--- Estoy fuera de mi funcion ---")

# Comprobar el acceso a la variable global
print(mensaje1)
# Intento acceder a mi variable local:
# print(mensaje2)