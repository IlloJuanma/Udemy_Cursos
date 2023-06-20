# Pareja de datos.
# Crear diccionario con usuarios y sus edades

edadesDeUsuarios = {"Pedro": 32, "Rosa" : 51, "Juan" : 23, "Jose" : 29}
print("Que edad tiene Pedro?:",edadesDeUsuarios["Pedro"])

# NO PODEMOS TENER KEYS REPETIDOS

# Forma alternativa de crear un diccionario : funcion dict()
misOtrasEdadesDeUsuarios = dict(Sara = 31, Antonio = 19, Marta = 35, Lucia = 48)
print("Que edad tiene Marta?:",misOtrasEdadesDeUsuarios["Marta"])

# Modificar una key de un diccionario
edadesDeUsuarios["Rosa"] = 52
print(edadesDeUsuarios["Rosa"])

# IMPORTANTE ES SENSIBLE A MAYUSCULAS Y MINUSCULAS

# Añadir key y valor
misOtrasEdadesDeUsuarios["Paco"] = 61
print(misOtrasEdadesDeUsuarios)

# Eliminar un valor
print("Lista antes de borrar a Juan:", edadesDeUsuarios)
del edadesDeUsuarios["Juan"]
print("Lista despues de borrar a Juan:",edadesDeUsuarios)

# Funciones extras
# Limpiar un diccionario
edadesDeUsuarios.clear()

# Saber cuales son mis keys en un diccionario
print("Los keys son:",misOtrasEdadesDeUsuarios.keys())

# Saber cuales son mis valores en un diccionario
print("Los valores son:",misOtrasEdadesDeUsuarios.values())

# Saber cuantos elementos tenemos en un diccionario
print("El numero de elementos son:",len(misOtrasEdadesDeUsuarios))