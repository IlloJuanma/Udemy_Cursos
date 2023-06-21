# Dado un numero introducido por el usuario, tenemos que imprimir por pantalla:
# Sus 5 primeros multiplos
# Su valor al cuadrado
# Su valor al cubo
# Su valor multiplicado por 100

numero = input("Hey! Introduce tu numero para que calcule cosas: ")
numero = float(numero)

print("Sus primeros cinco multiplos:",numero,numero*2,numero*3,numero*4,numero*5)
print("Su cuadrado y su cubo son:",numero**2,numero**3)
print("Su valor por 100:",numero*100)