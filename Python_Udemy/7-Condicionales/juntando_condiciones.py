usuario = input("Introduce tu usuario:")
contraseña = input("Introduce tu contraseña:")

if(usuario == "Juanma" and contraseña == "patata"):
    print("Bienvenido Juanma")
else:
    print("Usuario o contraseña incorrectos")

# Palabras clave que unen resultados/condiciones
# and - para que la condicion general se cumpla, todas las condiciones especificas tienen que ser verdaderas
# or - para que la condicion general se cumpla, al menos una de las especificas tienen que ser verdaderas

condicionA = 5 > 3
condicionB = 5 == 3

if(condicionA and condicionB):
    print("Todas las condiciones son verdaderas")
if(condicionA or condicionB):
    print("Al menos una de las condiciones es verdadera")>