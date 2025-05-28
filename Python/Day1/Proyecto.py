
Dolares = float(input( "Inregresa tus dolares a convertir: "))
Conversion = Dolares * 6

Billetes100 = 100
Billetes20 = 20

Recibir100 = Conversion // Billetes100
Recibir20 = Conversion % Billetes100
Recibir20 = Recibir20 // Billetes20
Pesos = Conversion - (Recibir100 * 100  + Recibir20 *20)  
print(f" recibiras en Euros la cantidad de {Conversion}")
print(f"Recibiras {Recibir100} de 100 y {Recibir20} billetes de 20 y {Pesos} en pesos")


