###  Dictionaries   ###
# Un diccionario es una colección desordenada de pares clave-valor.
# Cada clave es única y se utiliza para acceder a su valor correspondiente.
# Los diccionarios son mutables, lo que significa que puedes agregar, eliminar o modificar pares clave-valor después de su creación.
# La diferencia principal entre un diccionario y una lista o tupla es que los diccionarios utilizan claves para acceder a los valores en lugar de índices.

my_dict = dict()
my_other_dict = {}

my_dict = {"Nombre": "John", "Apellido": "Doe", "Edad": 30, 1: "Python"}
my_other_dict = {"Nombre": "Jane", 
                 "Apellido": "Doe", 
                 "Edad": 25,
                 "Lenguajes": {"Python", "Java", "C++"}} #Un diccionario puede contener cualquier tipo de dato, incluso otros diccionarios o sets 
print(my_dict)
print(my_other_dict)

print(len(my_dict)) #4. Número de pares clave-valor en el diccionario

# Acceder a los valores mediante sus claves
print(my_dict["Nombre"]) #John
print(my_dict[1]) #Python. Respeta el tipo de dato de la clave

# Modificar valores
my_dict["Nombre"] = "Mary" #Modifico el valor asociado a la clave "Nombre"
print(my_dict["Nombre"]) #Mary

# Agregar nuevos pares clave-valor
my_dict["Ciudad"] = "New York" #Añado un nuevo par clave-valor
print(my_dict)

# Eliminar pares clave-valor
del my_dict[1] #Elimino el par clave-valor con la clave 1
print(my_dict)

my_pop_element = my_dict.pop("Ciudad") #Elimino el par clave-valor con la clave "Apellido"
print(my_dict), print(my_pop_element) #New York

# Comprobar si una clave existe en el diccionario
print("Doe" in my_dict) #False. Comprueba claves, no valores
print("Apellido" in my_dict) #True

# Métodos útiles: los devuelve en listas
print(my_other_dict.items()) #dict_items([('Nombre', 'Jane'), ('Apellido', 'Doe'), ('Edad', 25), ('Lenguajes', {'C++', 'Java', 'Python'})])
print(my_other_dict.keys()) #dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes']) 
print(my_other_dict.values()) #dict_values(['Jane', 'Doe', 25, {'C++', 'Java', 'Python'}])
                              #El tipo de dato que devuelve es dict_vales pero se puede convertir a lista con list()
print(list(my_other_dict.values())) #['Jane', 'Doe', 25, {'C++', 'Java', 'Python'}]
# fromkeys
print(dict.fromkeys(("Nombre", 1, 2))) #{'Nombre': None, 1: None, 2: None} Crea un diccionario con las claves que le paso como argumento y valores None
                                       # Sirve para inicializar un diccionario con las mismas claves específicas
print(dict.fromkeys(("Nombre", 1, 2), 0)) #{'Nombre': 0, 1: 0, 2: 0} Igual que el anterior pero les ponemos un valor específico

# Ejemplo de uso de fromkeys: como inicializador de contador
vocales = ["a", "e", "i", "o", "u"]
contador = dict.fromkeys(vocales, 0) #Inicializo un diccionario con las vocales como claves y 0 como valor
print(contador)

# Mas métodos de diccionarios
my_dict.update({"Pais": "USA","Edad":31}) #Actualiza el diccionario con los pares clave-valor del diccionario que le paso
print(my_dict) #Si la clave ya existe, actualiza su valor. Si no existe, la añade
my_dict.update(Altura=1.75, Peso=80) #Otra forma de actualizar el diccionario, pasando los pares clave-valor como argumentos
print(my_dict)

print(list(my_dict)) #['Nombre', 'Apellido', 'Edad', 'Pais', 'Altura', 'Peso'] Devuelve una lista con las claves del diccionario


