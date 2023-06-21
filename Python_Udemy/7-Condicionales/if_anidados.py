miNombre = input("Es usted Juanma o Juan?")
miEdad = input("Que edad tiene?")

if(miNombre == "Juanma"):
    if(int(miEdad) < 10):
        print("Hola pequeño Juanma")
    elif(int(miEdad) < 22):
        print("Hola joven Juanma")
    else:
        print("Hola señor Juanma")
elif(miNombre == "Juan"):
    if(int(miEdad) < 10):
        print("Hola pequeño Juan")
    elif(int(miEdad) < 22):
        print("Hola joven Juan")
    else:
        print("Hola señor Juan")