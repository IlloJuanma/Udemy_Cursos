# Objetivo: decirle al usuario el precio que tendria que pagar por su entrada
# a un museo.
# Las tarifas son:
# Niño (hasta 6 años) :  no paga
# Joven (hasta 21 años) : 9€
# Adulto : 14€
# Jubilado (a partir de 67 años): 6€
# Además, hemos repartido unos descuentos en el ultimo mes del 10%. Si un usuario tiene un descuento y
# lo dice, tenemos que descontarle ese 10% del precio.
# Normas extra:
# - Si es un niño, no preguntar si tiene descuento o no. Si es gratis, es gratis
# - Si tiene descuento, mostrar precio con y sin descuento
# - Si no tiene descuento, mostrar unicamente el precio normal

# Ejemplo:
# >>Hola! Bienvenido al Museo de Python.
# >>
# >>Si quiere saber el precio de su entrada, por favor indique su edad: 37
# >>De acuerdo! Tiene usted el bono de descuento del 10% para este mes? (s/n): s
# >>
# >>El precio de su entrada sin descuenta es de 14.0€. Con el descuento, son 12.6€

"""
joven = 9
adulto = 14
jubilado = 6
adios = "Hasta luego!!"
print("Hola! Bienvenido al Museo de Python")
print("-----------")
edad = input("Si quiere saber el precio de su entrada, por favor indique su edad:")

if(int(edad) <= 6):
    print("Anda! La entrada es gratis para menores de 6 años :D")
    print(adios)
elif(int(edad) >=7 and int(edad) <=21):
    descuento = input("De acuerdo! Tiene usted el bono de descuento del 10%? (s/n):")
    if(descuento == "s"):
        print("El precio de su entrada sin descuento es:",joven,".Con descuento son ", joven-(joven*0.10))
        print(adios)
    else:
        print("El precio de su entrada es de ",joven)
        print(adios)
elif(int(edad) >=22 and int(edad) <=66):
    descuento = input("De acuerdo! Tiene usted el bono de descuento del 10%? (s/n):")
    if(descuento == "s"):
        print("El precio de su entrada sin descuento es:",adulto,".Con descuento son ", adulto-(adulto*0.10))
        print(adios)
    else:
        print("El precio de su entrada es de ",adulto)
        print(adios)
else:
    descuento = input("De acuerdo! Tiene usted el bono de descuento del 10%? (s/n):")
    if(descuento == "s"):
        print("El precio de su entrada sin descuento es:",jubilado,".Con descuento es ", jubilado-(jubilado*0.10))
        print(adios)
    else:
        print("El precio de su entrada es de ",jubilado)
        print(adios)
"""

# Otra forma mas eficiente sin repetir tanto codigo, repetir codigo NO!

print("Hola! Bienvenido al Museo de Python.\n")
edad = input("Si quiere saber el precio de su entrada, por favor indique su edad: ")
edad = int(edad)
precio = 0

if(edad <= 6):
    precio = 0
elif(edad <= 21):
    precio = 9
elif(edad <= 67):
    precio = 14
else:
    precio = 6

if(precio == 0):
    print("Menuda suerte, los niños entran gratis!")
else:
    descuento = input("De acuerdo! Tiene usted el bono descuento del 10%?(s/n):")
    if(descuento == "s"):
        precioDescuento = precio * 0.9
        print("El precio de su entrada sin descuento es de", precio, "€. Con el descuento son", precioDescuento)
    else:
        print("El precio de su entrada es de", precio, "€")