miLista = ["a","b","c","d"]

# Añadir un elemento a la lista : funcion append
miLista.append("e")
print("Tras añadir e:",miLista)

# Insertar un elemento en una posicion de la lista : funcion insert
miLista.insert(0,"x")
print("Tras añadir la x:",miLista)

# Eliminar un elemento por posicion : funcion del
del miLista[3]
print("Tras eliminar la posicion 3:", miLista)

# Combinar dos listas : funcion extend
miSegundaLista = ["a","f","g"]
miLista.extend(miSegundaLista)
print("Tras extender: ", miLista)

# Si nuestro elemento existe en nuestra lista : funcion in
print("Existe c en mi lista?")
resultado = "c" in miLista # True or false
print(resultado)
print("Existe x en nuestra lista?")
print("x" in miLista)

# Contar el numero de elementos que hay en nuestra lista : funcion len
numeroDeElementos = len(miLista)
print("Mi lista tiene %d elementos"%(numeroDeElementos))

# Eliminar un elemento concreto de mi lista por valor : funcion remove
miLista.remove("a")
print("Tras eliminar a :", miLista) # Quita la primera que encuentre
