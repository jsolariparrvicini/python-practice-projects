#main.py
from utils import *

contactos = cargar_contactos()
while True:
    mostrar_menu(1)
# Ejemplo de cómo se haría en tu bucle principal
    try:
        opcion_seleccionada = int(input("Seleccione una opción: "))
    except ValueError:
        print("\nError: Por favor, ingrese solo un número.")
        continue 
    if opcion_seleccionada < 1 or opcion_seleccionada > 6:
        print("\nError: Opción no válida, por favor seleccione una opción del 1 al 6.")
        continue


    match opcion_seleccionada:
        case 1:
            if not contactos:
                print("\nNo hay contactos para mostrar.")
            else:
                print("--- LISTA DE CONTACTOS ---")
                mostrar_contactos(contactos)
        case 2:
            if not contactos:
                print("\nNo hay contactos para buscar.")
            else:
                buscar_contacto(contactos)
        case 3:
            agregar_contacto(contactos)
        case 4: 
            if not contactos:
                print("\nNo hay contactos para actualizar.")
            else:   
                actualizar_contacto(contactos)
        case 5:
            if not contactos:
                print("\nNo hay contactos para eliminar.")
            else:
                eliminar_contacto(contactos)
        case 6:
            print("Saliendo del gestor de contactos. ¡Hasta luego!")
            if contactos:
                guardar_contactos(contactos)
            break

