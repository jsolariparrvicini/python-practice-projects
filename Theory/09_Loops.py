### Loops ###
# Los loops (bucles) son estructuras de control que nos permiten repetir un bloque de código varias veces.
# En Python, los dos tipos principales de loops son "for" y "while".    

# While , funciona mientras una condición sea verdadera.
my_condition = 0
while my_condition < 10:  #Mientras my_condition sea menor que 10, se ejecuta el bloque de código
    print(my_condition) 
    my_condition += 2 #Incremento my_condition en 2 para evitar un bucle infinito
else: #es opcional.
    print("La condición ya no es verdadera") #Se ejecuta cuando la condición deja de ser verdadera

print("\nFin del primer bucle while")  #Este código se ejecuta siempre, independientemente del while

while my_condition < 20:  
    print(my_condition) 
    my_condition += 2 
    if my_condition == 14:
        print(f"Mi condicion es {my_condition}, saliendo del bucle")
        break  #Rompe el bucle cuando my_condition es 14. Esto sirve para salir de un bucle si ocurre una condición específica.

# do-while: Python no tiene do-while, pero se puede simular con un while True y un break
print("\nSimulando do-while")
while True:
    print(f"Esto se ejecuta al menos una vez: {my_condition}")
    if my_condition >= 20: # Condición de salida del bucle
        print("Saliendo del bucle simulado do-while")
        break
    my_condition += 2  

# For , itera sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de texto).
my_list = [1, 2, 3, 4, 5] 
for element in my_list: #Está atado a cuantos elementos haya en la secuencia
    print(element)

print("\nIterando con tuplas")
my_tuple = (20, 1.80, "John", "Doe")
for element in my_tuple:
    print(element)

print("\nIterando con sets")
my_set = {23, 1.83, "John", "Doe"}
for element in my_set:  
    print(element)

print("\nIterando con diccionarios")
my_dict = {"Nombre": "John", "Apellido": "Doe", "Edad": 30}
for key in my_dict:  #Por defecto itera sobre las claves del diccionario
    print(key)
    if key == "Apellido":
        break  #Rompe el bucle cuando la clave es "Apellido"

for value in my_dict.values():  #Itera sobre los valores del diccionario
    print(value)

for key, value in my_dict.items():  #Itera sobre los pares clave-valor
    print(f"{key}: {value}")

print("\nIterando con cadenas de texto")
my_string = "Hola mundo"
for letter in my_string:  
    print(letter)
else: #es opcional.
    print("Se han iterado todos los elementos de la secuencia") #Se ejecuta cuando se han iterado todos los elementos de la secuencia 

#continue: salta a la siguiente iteración del bucle. Hoy en día se usa poco porque se puede evitar con condiciones.
print("\nUsando continue")
for element in my_list:
    if element == 3:
        print("Se ha encontrado el 3, saltando a la siguiente iteración")
        continue  #Salta a la siguiente iteración, salteando el código que queda en el bloque
    print(element)

# range: genera una secuencia de números, que es útil para iterar un número específico de veces en un bucle for.
print("\nUsando range")
for element in range(6):  #Genera números del 0 al 5 (6 no incluido)
    print(element)
for element in range(2, 6):  #Genera números del 2 al 5 (6 no incluido)
    print(element)

# nested loops: bucles dentro de bucles
print("\nUsando nested loops")
for i in range(1, 4):  #Bucle externo
    for j in range(1, 4):  #Bucle interno
        print(f"i: {i}, j: {j}")   
# Se pueden usar bucles anidados para iterar sobre estructuras de datos complejas, como listas de listas o diccionarios anidados.
# Sin embargo, hay que tener cuidado con el rendimiento, ya que los bucles anidados pueden aumentar exponencialmente el tiempo de ejecución.

#for con enumerate: itera sobre una secuencia y devuelve un par índice-valor en cada iteración, para ahorrar código.
print("\nUsando for con enumerate")
for index, element in enumerate(my_list):
    print(f"Índice: {index}, Elemento: {element}")
"""Usos comunes de los loops:
- Iterar sobre listas, tuplas, sets, diccionarios y cadenas de texto.
- Repetir una acción un número específico de veces.
- Procesar elementos en estructuras de datos complejas.
- Implementar algoritmos que requieren repetición, como búsquedas y ordenamientos.
- Automatizar tareas repetitivas, como procesamiento de archivos o generación de informes.
"""

