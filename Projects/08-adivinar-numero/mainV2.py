# main.py
import random # Importamos el módulo random para generar números aleatorios

numero_secreto = random.randint(1, 100) # Generamos un número aleatorio entre 1 y 100
intentos_permitidos = 5

print("¡Bienvenido al juego de Adivina el Número!")
print(f"Tenés {intentos_permitidos} intentos para adivinar el número entre 1 y 100.")

count_intento = 0 
while count_intento < intentos_permitidos:
    count_intento += 1
    intento = int(input(f"Intento {count_intento}. Ingresá tu número: "))
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número secreto!")
        break
    elif intento < numero_secreto: 
        print("El número secreto es más alto.")
    else :
        print("El número secreto es más bajo.")
else:
    print("\nSe te terminaron los intentos, no lo adivinaste.")
    print(f"El número secreto era {numero_secreto}")

