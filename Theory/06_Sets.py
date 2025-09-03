### Sets ###
# Un set es una colección desordenada de elementos únicos.
# No permite elementos duplicados y no mantiene un orden específico.
# Los sets son mutables, lo que significa que puedes agregar o eliminar elementos después de su creación.
# La diferencia principal entre un set y una lista o tupla es que los sets no permiten elementos duplicados y no mantienen un orden específico.

my_set = set()
my_other_set = {} #Los sets se definen con llaves {} a la vez que los diccionarios, pero los diccionarios tienen pares clave-valor.

print(type(my_set)) #<class 'set'>
print(type(my_other_set)) #<class 'dict'>

my_other_set = {23, 1.83, "John", "Doe"} 
print(type(my_other_set)) #<class 'set'> - Ahora es un set

# print(my_other_set[0]) #TypeError: 'set' object is not subscriptable. No puedo acceder a los elementos por índice porque no tienen un orden específico.

# Agregar elementos 
my_other_set.add("Python") #Añado un elemento al set de forma desordenada
print(my_other_set)
my_other_set.add(23) #No da error, pero no añade el elemento porque ya existe
print(my_other_set)

# Eliminar elementos
my_other_set.remove("Python") #Elimino un elemento del set. Da error si el elemento no existe
print(my_other_set)
my_other_set.discard("Python") #Elimino un elemento del set. No da error si el elemento no existe
print(my_other_set)
my_pop_element = my_other_set.pop() #Elimino un elemento aleatorio del set (porque no tienen orden). Devuelve el elemento eliminado
print(my_other_set)
print(my_pop_element)

#Busqueda de elementos
print(23 in my_other_set) #True. Compruebo si el elemento está en el set
print("Python" in my_other_set) #False. Compruebo si el elemento está en el set

my_other_set.clear() #Elimino todos los elementos del set
print(my_other_set)

del my_other_set #Elimino el set

# Operaciones con sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a | set_b) #Unión de sets (elementos únicos de ambos sets) {1, 2, 3, 4, 5, 6, 7, 8}
#print(set_a.union(set_b)) #Otra forma de hacer la unión
print(set_a & set_b) #Intersección de sets (elementos comunes a ambos sets) {4, 5}
print(set_a - set_b) #Diferencia de sets (elementos en set_a que no están en set_b) {1, 2, 3}
#print(set_a.difference(set_b)) #Otra forma de hacer la diferencia
print(set_a ^ set_b) #Diferencia simétrica (elementos en set_a o en set_b pero no en ambos) {1, 2, 3, 6, 7, 8}

#Eliminar duplicados de una lista usando sets
my_list = [1, 2, 2, 3, 4, 4, 5]
print(my_list) #[1, 2, 2, 3, 4, 4, 5]
my_list_no_duplicates = list(set(my_list)) #Elimino duplicados convirtiendo la lista a set y luego volviendo a convertirlo a lista
print(my_list_no_duplicates) #[1, 2, 3, 4, 5]
"""
Usos comunes de los sets:
- Eliminar duplicados de una lista o cualquier otra colección.
- Realizar operaciones matemáticas como unión, intersección y diferencia entre conjuntos de datos.
- Comprobar la pertenencia de un elemento de manera eficiente.
- Almacenar colecciones de elementos únicos, como etiquetas o categorías.
"""
