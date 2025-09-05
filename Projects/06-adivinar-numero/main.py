# main.py
import random # Importamos el módulo random para generar números aleatorios

numero_secreto = random.randint(1, 100) # Generamos un número aleatorio entre 1 y 100
intentos_permitidos = 5

print("¡Bienvenido al juego de Adivina el Número!")
print(f"Tenés {intentos_permitidos} intentos para adivinar el número entre 1 y 100.")

# Esto es un código repetitivo que se puede mejorar con bucles, pero aún no hemos visto ese concepto.

intento = int(input("Intento 1. Ingresá tu número: "))
if intento == numero_secreto:
    print("¡Felicidades! ¡Adivinaste el número secreto!")
    exit()
elif intento < numero_secreto:
    print("El número secreto es más alto.")
else :
    print("El número secreto es más bajo.")

intento = int(input("Intento 2. Ingresá tu número: "))
if intento == numero_secreto:
    print("¡Felicidades! ¡Adivinaste el número secreto!")
    exit()
elif intento < numero_secreto:
    print("El número secreto es más alto.")
else :
    print("El número secreto es más bajo.")

intento = int(input("Intento 3. Ingresá tu número: "))
if intento == numero_secreto:
    print("¡Felicidades! ¡Adivinaste el número secreto!")
    exit()
elif intento < numero_secreto:
    print("El número secreto es más alto.")
else :
    print("El número secreto es más bajo.")

intento = int(input("Intento 4. Ingresá tu número: "))
if intento == numero_secreto:
    print("¡Felicidades! ¡Adivinaste el número secreto!")
    exit()
elif intento < numero_secreto:
    print("El número secreto es más alto.")
else :
    print("El número secreto es más bajo.")

intento = int(input("Intento 5. Ingresá tu número: "))
if intento == numero_secreto:
    print("¡Felicidades! ¡Adivinaste el número secreto!")
    exit()
elif intento < numero_secreto:
    print("El número secreto es más alto.")
else :
    print("El número secreto es más bajo.")

print("\nSe te terminaron los intentos, no lo adivinaste.")
print(f"El número secreto era {numero_secreto}")