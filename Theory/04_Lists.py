### Lists ###
#Dos forms de declararlas
my_list = list()
my_other_list = [] 

print(len(my_list)) #0 #Longitud de la lista

my_list = [35, 24, 62, 52, 12, 24] #Lista de enteros
print(my_list) #[35, 24, 62, 52, 12]

my_other_list = [23, 1.83, "John", "Doe"] #Se pueden mezclar tipos de datos en un lista
age, height, name, surname = my_other_list #Desempaquetado de listas
print(name) #"John"

##Indexación y slicing (rebanado)##
#Los indices son como en las cadenas

print(my_other_list[0]) #23 #Accedo al primer elemento de la lista
print(my_other_list[-1]) #"Doe" #Accedo al último elemento de la lista
print(my_other_list[0:2]) #[23, 1.83] #Accedo a una porción de la lista (del índice 0 al 2, sin incluir el 2)
print(my_other_list[::-1]) #['Doe', 'John', 1.83, 23] #Accedo a toda la lista pero al revés (con paso -1)

##Funciones de listas##
print(my_list.count(24)) #2 #Cantidad de veces que aparece el elemento que le paso como argumento
print(my_list.index(24)) #1 #Índice del primer elemento que coincide con el valor que le paso como argumento
print(24 in my_list) #True #Compruebo si el valor que le paso como argumento está en la lista


#Agregado y eliminación de elementos
print(my_list + my_other_list) #[35, 24, 62, 52, 12, 24, 23, 1.83, 'John', 'Doe'] #Concatenación de listas

my_list.append(45) #Añado un elemento al final de la lista
print(my_list) 

my_list.insert(0, "hola") #Añado un elemento en la posición que le paso como primer argumento. (Posición 1, valor 67)
print(my_list)

my_list[0] = "adiós" #Cambio el valor del elemento en la posición que le paso como índice
print(my_list)

my_list.remove(24) #Elimino el elemento que le paso como argumento. Si hay varios iguales, elimina el primero que encuentra
print(my_list)

#pop
my_pop_element = my_list.pop() #Elimino el último elemento de la lista y lo guardo en una variable
print(my_list)
print(my_pop_element) 

print(my_list.pop(0)) #Elimino el elemento en la posición que le paso como argumento (posición 0)
print(my_list)

del my_list[0] #Elimino el elemento en el índice le paso como argumento (posición 0) =! a remove que elimina por valor
print(my_list)

my_new_list = my_list.copy() #Copio la lista en una nueva variable

my_list.clear() #Elimino todos los elementos de la lista
print(my_list)
print(my_new_list)

#Reverso y ordenamiento
my_other_list.reverse() #Le doy la vuelta a la lista
print(my_other_list)

my_new_list.sort() #Ordeno la lista de menor a mayor
print(my_new_list)
my_new_list.sort(reverse=True) #Ordeno la lista de mayor a menor
print(my_new_list)
#Ojo, no puedo ordenar listas que mezclen tipos de datos



