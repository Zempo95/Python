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
"""""
palabra = "murcielago"
print(palabra[0:6:2])
print(palabra[0::2])
print(palabra[0::0+1])
print(palabra[-7:-2])
print(palabra[7:2:-1])
#mclo
"""
"""
Extrae la subcadena "ciél" desde "murciélago" usando slicing.
Invierte la palabra y luego extrae los primeros 5 caracteres del resultado.
Extrae una subcadena que diga "góle" desde "murciélago" usando slicing y pasos negativos.
Construye la palabra "mago" usando solo slicing sobre "murciélago".
Elimina la primera y la última letra de "murciélago" usando slicing.
"""
palabra = "murcielago"
print(palabra[3:7])
print(palabra[-1:-10])

# ===============================
# Nivel Avanzado - Slicing en Python
# Palabra base: "murciélago"
# ===============================

palabra = "murciélago"
# Índices:      0123456789
# Letras:       m u r c i é l a g o

# 1️⃣ Extraer la subcadena "ciél"
# Tomamos desde el índice 3 ('c') hasta el índice 6 ('l'), sin incluir el 7
print("1. Subcadena 'ciél':", palabra[3:7])  # Resultado: 'ciél'

# 2️⃣ Invertir la palabra y extraer los primeros 5 caracteres
# Invertimos la palabra con [::-1] y luego tomamos los primeros 5 con [:5]
print("2. Primeros 5 caracteres invertidos:", palabra[::-1][:5])  # Resultado: 'ogale'

# 3️⃣ Extraer una subcadena que diga "góle" usando slicing y pasos negativos
# Del índice 8 ('g') al índice 5 ('é') en orden inverso: [8:4:-1]
print("3. Subcadena invertida (góle al revés):", palabra[8:4:-1])  # Resultado: 'gólé'
# Si se desea en orden "normal", se puede invertir el resultado:
print("3b. 'góle' en orden directo (si existiera):", palabra[8:4:-1][::-1])  # Resultado: 'élóg'

# 4️⃣ Construir la palabra "mago" usando slicing
# Tomamos letras específicas: 'm' (0), 'a' (7), 'g' (8), 'o' (9)
print("4. Construir 'mago':", palabra[0] + palabra[7] + palabra[8] + palabra[9])  # Resultado: 'mago'

# 5️⃣ Eliminar la primera y la última letra
# Saltamos la primera (índice 0) y la última (índice -1) usando [1:-1]
print("5. Sin primera ni última letra:", palabra[1:-1])  # Resultado: 'urciélag'
