### Strings ###
new_line_string = "This is a string\nwith a new line" #\n es un carácter especial que representa un salto de línea
print(new_line_string)

tab_string = "This is a string\twith a tab" #\t es un carácter especial que representa una tabulación
print(tab_string)

scape_string = "This is a string with a backslash \\n " # \\ escapa el siguiente carácter especial
print(scape_string)

##Formateo##
name, surname, age = "John", "Doe", 20
print("Mi nombre es %s %s y tengo %d años" % (name, surname, age)) #Forma antigua de formateo
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age)) #Forma clásica de formateo
print(f"Mi nombre es {name} {surname} y tengo {age} años") #Forma moderna de formateo (f-strings)

a,b = 5, 3
print(f"El resultado de {a} + {b} es {a + b}") 
print(f"El resultado de {a} / {b} es {a / b:.2f}") #:.2f es una forma de formatear números en Python usando f-strings.

##Desempaquetado de caracteres##
word = "python"
a, b, c, d, e, f = word
print(a)
print(f)
print(a + b + c + d + e + f)

##Indexación y slicing (rebanado)##
print(word[0]) #Accedo al primer caracter de la cadena (índice 0)
print(word[-1]) #Accedo al último caracter de la cadena (índice -1)
print(word[0:2]) #Accedo a una porción de la cadena (del índice 0 al 2, sin incluir el 2)
print(word[2:]) #Accedo a una porción de la cadena (desde el índice 2 hasta el final)
print(word[::]) #Accedo a toda la cadena
#Evito caracteres
print(word[1:6:2]) #Accedo a una porción de la cadena (del índice 1 al 6, incluyendo el último caracter, con paso 2)
#Revés
print(word[::-1]) #Accedo a toda la cadena pero al revés (con paso -1)
print(word[:0:-1]) #Accedo a toda la cadena pero al revés (con paso -1), sin incluir el primer caracter

##Funciones de strings##
print(len(word)) #Cantidad de caracteres
print(word.capitalize()) #Primera letra en mayúscula
print(word.upper()) #Todo en mayúscula
print(word.lower()) #Todo en minúscula


print(word.count("t")) #Cantidad de veces que aparece el caracter "t"
print("aaa".count("a")) #3

print(word.isnumeric()) #False, si la cadena es numérica
print("123".isnumeric()) #True, si la cadena es numérica
print(word.isalpha()) #False, si la cadena es alfabética

#combinar funciones
print(word.upper().isupper()) #True, si la cadena es mayúscula
print(word.capitalize().isupper()) #False, si la cadena es mayúscula

print(word.startswith("py")) #True, si la cadena empieza con "py"
print(word.endswith("on")) #True, si la cadena termina con "on"

print(word.find("th")) #Índice donde empieza la subcadena "th" (2). Si no lo encuentra devuelve -1
print(word.find("xx")) #No lo encuentra (-1)

print(word.replace("thon","py")) #Reemplaza "thon" por "py" (pypy). Reemplaza todas las ocurrencias.
print("python python".replace("thon","py",1)) #Reemplaza "thon" por "py" (pypy python). Reemplaza la primera ocurrencia.

print("   python   ".strip()) #Elimina los espacios en blanco al inicio y al final
print("   python   ".lstrip()) #Elimina los espacios en blanco al inicio
print("   python   ".rstrip()) #Elimina los espacios en blanco al final