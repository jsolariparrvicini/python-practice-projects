#main.py
import random
# Códigos de colores para la consola
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
GREY = '\033[90m'
RESET = '\033[0m' 

# Lista de palabras de 5 letras
palabras = ["JUEGO","LISTA","AUDIO","IDEAS","COSAS","MANOS","LETRA","LIBRO","NUNCA","PLUMA","LLAVE","MENTE","LUCES",
            "GATOS","PERRO","QUESO","BRAVO","FLOTA","GRITO","HUEVO"]
cantidad_intentos = 6
palabra_adivinar = random.choice(palabras)

print("¡Bienvenido a Wordle de Consola!")
for i in range(cantidad_intentos):
    palabra_intento = input(f"\nIntento {i + 1}/6: Ingresa una palabra de 5 letras: ").strip() # Pedir al usuario que ingrese una palabra
    while len(palabra_intento) != 5 or not palabra_intento.isalpha(): # Validar que la palabra tenga 5 letras y solo contenga letras
        print("Error: La palabra debe tener exactamente 5 letras alfabéticas. Inténtalo de nuevo.")
        palabra_intento = input(f"Intento {i + 1}/6: Ingresa una palabra de 5 letras: ").strip()
    
    palabra_intento = palabra_intento.upper() 
    if palabra_intento == palabra_adivinar: # Verificar si la palabra es correcta. Si es correcta, felicitar al usuario y terminar el juego
        print(f"{GREEN}¡Felicidades! ¡Adivinaste la palabra secreta: {palabra_adivinar}!{RESET}")
        break
    print("Feedback: ", end="")
    for index,caracter in enumerate(palabra_intento): # Proporcionar feedback al usuario. Usamos colores para indicar si las letras están en la posición correcta, si están en la palabra pero en la posición incorrecta, o si no están en la palabra
        if caracter == palabra_adivinar[index]:
            print(f"{GREEN}{caracter}{RESET}", end=" ") 
        elif caracter in palabra_adivinar:
            print(f"{YELLOW}{caracter}{RESET}", end=" ")
        else:
            print(f"{GREY}{caracter}{RESET}", end=" ")
        
else: 
    print(f"\n{RED}Se te terminaron los intentos, no lo adivinaste.{RESET}")
    print(f"La palabra secreta era: {palabra_adivinar}")


