# Comprobar si dos elementos son iguales o no
# ==
print("Es 5 == 5?-->",5 == 5)
print("Es 6 == 5?-->",6 == 5)

# Comprobar si dos elementos son diferentes
# !=
print("Es 5 != 5?-->",5 != 5)
print("Es 6 != 5?-->",6 != 5)

# Comprobaciones aritmeticas: mayor que, menor o igual que, menor que, menor o igual que
# >, >=, <, <=
print("Es 5 >= 2?-->", 5>2)
print("Es 5 >= 10?-->", 5>10)
print("Es 5 <= 2?-->", 5<2)
print("Es 5 <= 10?-->", 5<10)

# La comprobacion "in", si esta dentro de otra cosa o no
miString="abcdefgh"
print("Esta p dentro de mi string?", "b" in miString)
miNuevaString = "Mi amigo Jose tiene un pato que se llama Pepe"
print("Esta pato dentro de miNuevaString?", "pato" in miNuevaString)

# Sintaxtis : if(condicion)

if(5==5):
    print("Cierto!")
    print("Otro String de prueba")
else:
    print("No es cierto")

miNombre = "Juanma"
if(miNombre == "Jose"):
    print("Hola muchacho")
elif(miNombre=="Juanma"):
    print("Hola Juanma")
elif(miNombre=="Paco"):
    print("Hola profesor")
else:
    print("No te conozco pero hola")
