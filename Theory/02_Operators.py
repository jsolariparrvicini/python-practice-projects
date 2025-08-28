### Operators ###
##Operadores aritméticos##
#Operadores básicos como un +, -, * y /
print(3*2), print(2 + 5)

#Operador módulo % : resto de una división
print(10 % 3) #Util para saber si hay un múltiplo

#Operador "flor division" // : División entera, la cual redonde pra abajp (ej: si el resultado es 9.2, devuelve 9. Lo mismo si es 9.9)
print(10 // 3)
print(-7 // 2) #-3.5 lo redondea a -4

#Operador exponencial **
print (2 ** 3)

#Operaciones con strings
print("Hola" + " Python") #Concatena strings (no puedo mezclar tipos de datos)
print("Hola " * 3) #Repite el string 3 veces
print("Numero: " + str(5))
print( len("Hola") + 5)

##Operadores Comparativos##
print(3 < 4), print( 3 > 4), print(3 >= 4), print(3 == 4), print(3 != 4)
print("hola" > "python") #Ordenación alfabética por ASCII(tiene en cuenta las mayúsculas también)
print("hola" < "python")
print("hola" != "python")
print("hola" == "hola")

##Operadores Lógicos##
print(3 > 4 and "hola" > "python")
print(3 > 4 or "hola" > "python")
print(not(3 > 4))
print(3 > 4 or "hola" > "python" or 4 == 4)
print("" or "python") # "Python"  (porque "" es "falso"): "else"
print("hola" and 1) # 1 porque es el que hace cumplir la condición: "if"

print("mundo" in "Hola mundo") #El operador in devuelve True si el primer string está contenido en el segundo. No solo funciona con strings, también con listas y otros tipos de datos.

print(str(bool(1)))

#:.2f es una forma de formatear números en Python usando f-strings.
# : → empieza el formato.
# .2 → significa 2 decimales.
# f → significa que se muestre como número decimal de punto fijo (float).

print(f"El resultado es {3.14159:.2f}") #El resultado es 3.14

#Uso de and y or como operadores cortocircuitados
# and devuelve el primer valor falso o el último valor verdadero
print(0 and "Hola") #0
print(1 and "Hola") #"Hola"
print(1 and 2 and 3 and 0 and 5) #0
print(1 and 2 and 3 and 4 and 5) #5 
# or devuelve el primer valor verdadero o el último valor falso
print(0 or "Hola") #"Hola"
print("" or "Hola") #"Hola"
print(0 or "" or [] or None or "Python") #"Python"

#Ejemplo de uso en vez de if y else
edad = 18
es_mayor = (edad >= 18 and "Es mayor de edad") or "Es menor de edad"
print(es_mayor) #"Es mayor de edad"