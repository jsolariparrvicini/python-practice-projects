#variables: En minúscula y guiones bajos. Ej, en vez de myVarible, es mejor práctica my_variable
my_string_variable = "My first variable!"
print(my_string_variable)

my_int_variable = 2
print(my_int_variable)

#Se le pueden pasar multiples argumentos al print, el cual concatena las var en una única caden
print(my_string_variable,"is",my_int_variable)

print(f"my variable is {my_int_variable}")

#variables en una sola línea ( no es la mejor práctica ). Tiene + sentido en funciones que me devuelven más de un valor y los quiero desempaquetar.
name, surname = "John", "Doe"
print ("My name is: ",name,surname)

#Algunas funciones del sistema
#Función str() convierte el tipo de dato a str. De la misma forma existen las funciones int() o float()
my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

#Función len() me da la cantidad de caracteres de una cadena de texto
print(len(my_string_variable))

#Función list() convierte cada caracter de la cadena en un elemento de la lista
print(list(name))

#Función input() le pide al usuario que ingrese un valor por consola
# user_name = input("What's your name? ")
# print(f"User name is {user_name}") 

# user_age = int(input("What's your age?")) # OJO! input() devuelve un string.
# print(user_age)
