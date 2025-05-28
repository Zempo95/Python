nombre = str(input("Inregresa tu nombre: "))
fecha = str(input("Ingresa la fecha: "))
saludo = "Buenos dias"
billetecien = 100
billetesveinte = 20


print(f"{saludo}  {nombre}")
dolares = float(input("Ingresa aquí los dolares: "))
dolarestoeuros = dolares * 4
print(f"tu cambio de divisa es por: {dolarestoeuros} ")

billeteCien = dolarestoeuros / billetecien
billetesVeinte= dolares % billetesveinte

print(f"USted recibira {billeteCien} de cien y {billetesVeinte} billestes de veinte")





