# A partir de 5 datos dados en variables, obtener el precio de un deposito de gasolina
# Imprimir el precio para que parezca una factura
# Componerlo todo en una unica string
# ----------------------------------
precio = "1.394934"
litros = 44.59
surtidor = 17.0
combustible = "diesel"

# Hacer type cast necesarios:
precio = float(precio)
surtidor = int(surtidor)

# Calcular el importe total:
importeTolal = litros * precio

# Componer factura
linea1 = "--------Factura--------"
linea2 = "Combustible: {}".format(combustible.upper())
linea3 = "Precio %.3f €/l"%(precio)
linea4 = "Litros: %.2f"%(litros)
linea5 = "Surtidor: " +str(surtidor)
linea6 = "Importe total: %.2f €"%(importeTolal)
linea7 = "-----------------------"

miFactura = linea1+"\n"+linea2+"\n"+linea3+"\n"+linea4+"\n"+linea5+"\n"+linea6+"\n"+linea7
print(miFactura)