# Tenemos una lista con nombres de ciudades:
ciudadesDeEspaña = ["Granada","Córdoba","Santiago de Compostole", "París", "Málaga", "Barcelona"]
otrasCiudades = ["Toledo", "Sevilla","Cádiz","Berlin","Alicante"]

# Tareas:
# 1 - Quitar de las listas las ciudades que no pertenezcan a España (Berlín y París)
# 2 - Unir ambas listas en una unica
# 3 - Añadir Madrid, la capital, en la primera posicion de la lista
# 4 - Añadir otras tres ciudades a tu eleccion
# 5 - Imprimir la siguiente frase por pantalla
# >> Mi lista de ciudades tiene {numero de ciudades aqui} ciudades: [Contenido de la lista]

ciudadesDeEspaña.remove("París")
otrasCiudades.remove("Berlin")

ciudadesDeEspaña.extend(otrasCiudades)
ciudadesDeEspaña.insert(0,"Madrid")
#ciudadesDeEspaña.append("Mallorca")
#ciudadesDeEspaña.append("Santander")
#ciudadesDeEspaña.append("Burgos")
nuevaLista=["Mallorca","Santader","Burgos"]
ciudadesDeEspaña.extend(nuevaLista)
print("Mi lista de ciudades tiene %d ciudades: "%(len(ciudadesDeEspaña)),ciudadesDeEspaña)