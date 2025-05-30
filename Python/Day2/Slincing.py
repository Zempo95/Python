#Dada la palabra "murciélago", imprime la letra en la posición 6.
#Extrae los primeros 4 caracteres de "murciélago".
#Extrae la última letra usando índice negativo.
#Imprime la palabra "murciélago" al revés.
#Extrae los caracteres del índice 2 al 6 (sin incluir el 6).
# m-0
# u-1
# r-2
# c-3
# i-4
# e-5
# l-6
# a-7
# g-8
# o-9
"""
palabra = "murcielago"
print(palabra[6])
print(palabra[0:4])
print(palabra[-1])
print(palabra[::-1])
print(palabra[2:6])
"""

#Extrae los primeros 6 caracteres de "murciélago" saltando de 2 en 2.
#Extrae todos los caracteres en posiciones pares (índices 0, 2, 4...) de "murciélago".
#Extrae todos los caracteres en posiciones impares.
#Imprime la palabra desde el índice 7 hasta el 2 en orden inverso.
#¿Qué imprime "murciélago"[::3]?

palabra = "murcielago"
print(palabra[0:6:2])
print(palabra[0::2])
print(palabra[0::0+1])
print(palabra[-7:-2])
#mclo
