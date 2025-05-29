
palabra = "aventura" 
print(palabra [1:6:2].upper()) 
cadena = "pythonista"
print(cadena[2:2+4])  # 'thon'
palabra = "elefante"

# 1. Imprime la letra en la posición 3
print(palabra[3])  # f

# 2. Extrae los últimos 4 caracteres
print(palabra[-4:])  # ante

# 3. Extrae la subcadena desde la posición 1 hasta la 5 (sin incluir 5)
print(palabra[1:5])  # lefa

# 4. Imprime la palabra al revés usando slicing
print(palabra[::-1])  # etnafele

# 5. Extrae cada tercer carácter empezando desde el índice 0
print(palabra[0::3])  # eft