
Dolares = float(input( "Inregresa tus dolares a convertir: "))
conversion = Dolares * 6

Billetes100 = 100
Billetes20 = 20

Recibir100 = conversion // Billetes100
Recibir20 = conversion % Billetes100
Recibir20 = Recibir20 // Billetes20

print(f"Recibiras {Recibir100} de 100 y {Recibir20} billetes de 20")


