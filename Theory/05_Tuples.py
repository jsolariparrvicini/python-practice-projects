### Tuples ###
# Una tupla es una colección ordenada e inmutable de elementos.
# Las tuplas pueden contener elementos de diferentes tipos de datos.
#Es INMUTABLE a diferencia de las listas. No se pueden modificar, agregar o eliminar elementos después de su creación.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1.83, "John", "Doe")
print(my_tuple)
print(my_tuple[0]), print(my_tuple[-1]), print(my_tuple[0:2]), print(my_tuple[::-1])

print(my_tuple.count(23))
print(my_tuple.index("John"))

# my_tuple[0] = 34 #TypeError: 'tuple' object does not support item assignment. Es declarada como inmutable.

# Concatenación de tuplas
my_other_tuple = (34, 56, 12)
my_sum_tuple = my_tuple + my_other_tuple #Concatenación de tuplas
print(my_sum_tuple)

#Convertir una tupla en una lista
my_tuple_to_list = list(my_sum_tuple)
print(my_tuple_to_list)

#Modificar la lista y volver a convertirla en tupla
my_tuple_to_list[0] = 34
my_tuple_to_list.insert(0,"Rojo")
print(tuple(my_tuple_to_list)) #Vuelvo a convertir la lista en una tupla para que sea inmutable

#Eliminar la tupla. No es lo ideal, pero sirve para entender que son inmutables
del my_tuple
# print(my_tuple) #NameError: name 'my_tuple' is not defined

"""
Usos comunes de las tuplas:
- Almacenar datos que no deben cambiar a lo largo del programa, como coordenadas geográficas (latitud y longitud), fechas (día, mes, año) o colores RGB (rojo, verde, azul).
- Retornar múltiples valores desde una función.
- Usar como claves en diccionarios, ya que las tuplas son hashables (a diferencia de las listas). 
  Hashable significa que su valor no cambia durante su vida útil, lo que permite que se utilicen como claves en estructuras de datos como diccionarios y conjuntos.
- Desempaquetado de tuplas para asignar valores a múltiples variables de manera concisa.
"""