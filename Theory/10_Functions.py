##  FUNCTIONS ##
# Una función es una relación entre un conjunto de entradas y un conjunto de salidas
# Una función toma una entrada, realiza alguna operación y devuelve una salida
# Las funciones nos permiten reutilizar código y evitar la repetición
# En Python, las funciones se definen usando la palabra clave 'def' 

def  my_function ():
    print("Esto es una función")

my_function()

# Funciones con parámetros
def sum_two_values (a,b):
    print(a + b)

sum_two_values(3,4)

# Funciones con retorno
def sum_two_values_return (a,b):
    return a + b

my_result = sum_two_values_return(3,5) # Almacenar el valor retornado en una variable
print(my_result)

# Funciones con valores por defecto
def sum_with_default (a,b=5): # b tiene un valor por defecto de 5
    return a + b
print(sum_with_default(1)) # Usar el valor por defecto
print(sum_with_default(1,3)) # Sobrescribir el valor por defecto

# Funciones con múltiples retornos
def multiple_returns (a,b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result # Retornar múltiples valores como una tupla

print(multiple_returns(2,3)) # Retorna una tupla (5,6)
sum_val, prod_val = multiple_returns(2,3) # Desempaquetar la tupla en variables separadas
print(f"Suma: {sum_val}, Producto: {prod_val}")

# Funciones recursivas
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # 120

# Funciones lambda (funciones anónimas)
add = lambda x, y: x + y # La función lambda toma dos parámetros y retorna su suma. Sirven para funciones simples de una sola línea 
print(add(2,3)) # 5

# Uso de funciones integradas
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers)) # Usar map para aplicar una función a cada elemento de una lista
print(squared) # [1, 4, 9, 16, 25] 

filtered = list(filter(lambda x: x % 2 == 0, numbers)) # Usar filter para filtrar elementos de una lista
print(filtered) # [2, 4]


#Parametros * 
def func_with_args(*args): #Le puedo pasar cualquier cantidad de argumentos
    for arg in args:
        print(arg, end=" ")

func_with_args(1,2,3,4,5)



