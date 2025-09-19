#main.py
from gestor import Contacto, GestorContactos

def mostrar_menu(num_menu):
    if num_menu == 1:
        print(""" 
    --- GESTOR DE CONTACTOS ---
    1. Ver lista de contactos
    2. Buscar contacto
    3. Agregar nuevo contacto
    4. Actualizar contacto
    5. Eliminar contacto
    6. Salir
    """) #Los tres comillas permiten hacer un string multilínea
    elif num_menu == 2:
        print(""" 
    \n¿Qué dato desea modificar?
    1. Nombre
    2. Apellido
    3. Teléfono
    4. Email
    5. Cancelar
    """)

def main():
    gestor_contactos = GestorContactos() #Crea una instancia de GestorContactos, que carga los contactos desde el archivo JSON si existe.
    while True:
        mostrar_menu(1)
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
                gestor_contactos.mostrar_contactos()
            case 2:
                print("\n--- Buscar Contacto ---")
                termino_busqueda = input("Ingrese el nombre o apellido a buscar: ")
                print(f"\nResultados de la busqueda para '{termino_busqueda}'")

                contactos_encontrados = gestor_contactos.buscar_contacto(termino_busqueda)
                if contactos_encontrados:
                    gestor_contactos.mostrar_contactos(contactos_encontrados)
                else:
                    print(f"No se encontraron contactos que coincidan con '{termino_busqueda}'")
            case 3:
                print("\n--- Agregar Nuevo Contacto ---")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")  

                nuevo_contacto = Contacto(nombre,apellido,telefono,email)    
                gestor_contactos.agregar_contacto(nuevo_contacto)      
            case 4: 
                print("\n--- Actualizar Contacto ---")
                termino_busqueda = input("Ingrese el nombre o apellido a actualizar: ")
                print(f"\nResultado de la busqueda para '{termino_busqueda}'")

                contactos_encontrados = gestor_contactos.buscar_contacto(termino_busqueda)
                if len(contactos_encontrados) == 1: 
                    contacto_a_actualizar = contactos_encontrados[0]
                    print(f"Contacto encontrado: {contacto_a_actualizar}")
                    mostrar_menu(2)
                    while True:
                        try:
                            opcion_submenu = int(input("Seleccione una opción para modificar: "))
                            if 1 <= opcion_submenu <= 5:
                                break
                            else:
                                print("Error: Opción no válida, por favor seleccione una opción del 1 al 5.")
                        except ValueError:
                            print("Error: Por favor, ingrese solo un número.")  

                    match opcion_submenu:
                        case 1:
                            nuevo_valor = input("Ingrese el nuevo nombre: ")
                            campo = "nombre"
                        case 2:
                            nuevo_valor = input("Ingrese el nuevo apellido: ")
                            campo = "apellido"
                        case 3:
                            nuevo_valor = input("Ingrese el nuevo teléfono: ")
                            campo = "telefono"
                        case 4:
                            nuevo_valor = input("Ingrese el nuevo email: ")
                            campo = "email"
                        case 5:
                            print("Operación cancelada.")
                            continue
                    gestor_contactos.actualizar_contacto(contacto_a_actualizar,campo,nuevo_valor)
                elif len(contactos_encontrados) > 1:
                    print("Demasiados contactos encontrados. Por favor, sea más específico.")
                    gestor_contactos.mostrar_contactos(contactos_encontrados)   
                    continue
                else:       
                    print(f"No se encontraron contactos que coincidan con '{termino_busqueda}'")
                    continue
            case 5:
                print("\n--- Eliminar Contacto ---")
                termino_busqueda = input("Ingrese el nombre o apellido a eliminar: ")
                print(f"\nResultado de la busqueda para '{termino_busqueda}'")
                
                contactos_encontrados = gestor_contactos.buscar_contacto(termino_busqueda)
                if len(contactos_encontrados) == 1: 
                    contacto_a_eliminar = contactos_encontrados[0]
                    print(f"Contacto encontrado: {contacto_a_eliminar}")
                    confirmacion = input("¿Está seguro que desea eliminar este contacto? (s/n): ")
                    if confirmacion.lower() == 's':
                        gestor_contactos.eliminar_contacto(contacto_a_eliminar)
                    else:
                        print("Operación cancelada.")
                        continue
                elif len(contactos_encontrados) > 1:
                    print("Demasiados contactos encontrados. Por favor, sea más específico.")
                    gestor_contactos.mostrar_contactos(contactos_encontrados)   
                    continue
                else:       
                    print(f"No se encontraron contactos que coincidan con '{termino_busqueda}'")
                    continue
            case 6:
                print("Saliendo del gestor de contactos. ¡Hasta luego!")
                gestor_contactos.guardar_contactos() #Guarda los contactos en el archivo JSON antes de salir
                break

if __name__ == "__main__":
    main()