###  Conditionals   ###
## Estructuras de control condicionales: if, elif, else
# Permiten ejecutar bloques de código dependiendo de si una condición es verdadera o falsa

my_condition = True

if my_condition:  #Si my_condition es True, se ejecuta el bloque de código
    print("Se ejecuta el if")
else:  #Si my_condition es False, se ejecuta el bloque de código del else
    print("Se ejecuta el else")
print("Sigo con el programa")  #Este código se ejecuta siempre, independientemente del if-else

my_condition = 5 * 2

# Elif: else if. Permite comprobar múltiples condiciones
if my_condition == 11:
    print("La condición es igual  11") 
elif my_condition == 10:
    print("La condición es igual a 10")
else :
    print("La condición no es ni 10 ni 11")

my_condition = 5 * 3
#  Condiciones con and y or
if my_condition > 10 and my_condition < 20:  
    print("La condición es mayor a 10 y menor a 20")

if my_condition > 10 or my_condition < 15:  
    print("La condición es mayor a 10 o menor a 15")

#  Condición con not
if not my_condition == 10:  
    print("La condición no es igual a 10")

# Condiciones in y not in
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("El 3 está en la lista")
if 6 not in my_list:
    print("El 6 no está en la lista")
 
# Condiciones anidadas
my_string = "Hola mundo"
if my_string.startswith("H"):
    if my_string.endswith("o"):
        print("La cadena empieza con H y termina con o")
    else:
        print("La cadena empieza con H pero no termina con o")

# Evitar anidar condicionales usando operadores lógicos
if my_string.startswith("H") and my_string.endswith("o"):
    print("La cadena empieza con H y termina con o")
else:
    print("La cadena no cumple ambas condiciones")

#Operador ternario (condición en una sola línea)
my_value = 10
print("Es mayor a 10") if my_value > 10 else print("No es mayor a 10")
# Tambien se puede usar para asignar valores a variables
my_other_value = "Es mayor a 10" if my_value > 10 else "No es mayor a 10"
print(my_other_value)
