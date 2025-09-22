## Exceptions ##
# Manejo de errores y excepciones en Python
# Permite manejar errores de manera controlada sin que el programa se detenga abruptamente.
# Se usan bloques try, except, else y finally.

# Ejemplo básico
try:
    print(5 + "5") #Esto genera un TypeError
except TypeError:
    print("Error: No se pueden sumar un número y una cadena de texto.")
else: #opcional
    print("La suma se realizó correctamente.") # Se ejecuta si no hubo errores en el bloque try
finally: #opcional
    print("Este bloque se ejecuta siempre, haya o no error.") # Se ejecuta siempre, haya o no error

# Capturar múltiples excepciones por tipo. Si no se especifica el tipo, captura cualquier excepción.
try:    
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
except ValueError:
    print("Error: Debe ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("Fin del programa.")

# Capturar información del error
try:
    lista = [1, 2, 3]
    print(lista[5]) #Esto genera un IndexError
except IndexError as e: #Capturo la excepción coN "as e"
    print(f"Error: {e}") #Muestra el mensaje del error

# Lanzar excepciones con raise
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.") #Lanza una excepción ValueError con un mensaje personalizado
    return a / b    
 #Raise se usa para lanzar excepciones de manera explícita.
# Se puede usar para validar entradas o condiciones específicas en funciones.
try:
    print(dividir(10, 0))
except ValueError as e:
    print(f"Error al dividir: {e}")

# Usos:
# Validar entradas de usuario
# Manejar errores en operaciones de archivo
# Controlar errores en operaciones de red
# Implementar lógica de recuperación ante fallos
# Crear excepciones personalizadas para casos específicos de la aplicación