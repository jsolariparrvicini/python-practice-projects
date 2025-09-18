def guardar_contactos(contactos):
    with open("contactos.txt", 'w') as archivo:
        for contacto in contactos:
            linea = f"{contacto['nombre']},{contacto['apellido']},{contacto['telefono']},{contacto['email']}\n"
            archivo.write(linea)

def cargar_contactos():
    contactos = [] 
    try:
        with open("contactos.txt", 'r') as archivo:
            lineas = archivo.readlines() #Creamos una lista con cada línea del archivo
            for linea in lineas:
                linea = linea.strip().split(",") #Eliminamos espacios y saltos de línea, y separamos por comas creando una lista
                contacto = {"nombre": linea[0], "apellido": linea[1], "telefono": linea[2], "email": linea[3]} #Creamos un diccionario con los datos del contacto
                contactos.append(contacto)

    except FileNotFoundError:       
        print("Archivo no encontrado, empezando con una lista vacía.")
    return contactos

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
        
def mostrar_contactos(contactos):
    print("----------------")
    for index,contacto in enumerate(contactos):
        print(f"{index + 1}. Nombre: {contacto['nombre']}, Apellido: {contacto['apellido']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    print("----------------")

def buscar_contacto(contactos):
    print("--- Buscar Contacto ---")
    termino_busqueda = input("Ingrese el nombre o apellido a buscar: ")
    print(f"\nResultados de la busqueda para '{termino_busqueda}'")
    contactos_encontrados = []
        
    for contacto in contactos: # Busco todos los contactos que coincidan con el término de búsqueda
        nombre_completo = f"{contacto['nombre']} {contacto['apellido']}"
        if termino_busqueda.lower() in nombre_completo.lower():
            contactos_encontrados.append(contacto)
    if contactos_encontrados:
        mostrar_contactos(contactos_encontrados)
    else:
        print(f"\nNo se encontraron contactos que coincidan con '{termino_busqueda}'")

def agregar_contacto(contactos):
    print("--- Agregar Nuevo Contacto ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    
    for contacto in contactos:
        if telefono == contacto['telefono']: #Verifico que no exista otro contacto con el mismo teléfono
            print("\nYa existe un contacto con ese número de teléfono. No se puede agregar el contacto.")
            return
        elif email.lower() == contacto['email'].lower(): #Verifico que no exista otro contacto con el mismo email
            print("\nYa existe un contacto con ese email. No se puede agregar el contacto.")
            return
    nuevo_contacto = {"nombre": nombre, "apellido": apellido, "telefono": telefono, "email": email}
    contactos.append(nuevo_contacto)
    print(f"Contacto '{nombre} {apellido}' agregado exitosamente.")


def actualizar_contacto(contactos):
    print("--- Actualizar Contacto ---")
    termino_busqueda = input("Ingrese el nombre o apellido a actualizar: ")
    print(f"\nResultado de la busqueda para '{termino_busqueda}'")

    contactos_encontrados = []
    for contacto in contactos: # Busco todos los contactos que coincidan con el término de búsqueda
        nombre_completo = f"{contacto['nombre']} {contacto['apellido']}"
        if termino_busqueda.lower() in nombre_completo.lower():
            contactos_encontrados.append(contacto)

    if len(contactos_encontrados) == 1: #Si solo hay un contacto que coincide, procedo a actualizarlo
        contacto_actualizar = contactos_encontrados[0]
        print("Contacto encontrado: ")
        mostrar_contactos(contactos_encontrados)
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
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                contacto_actualizar['nombre'] = nuevo_nombre
                print("Nombre actualizado exitosamente.")
            case 2:
                nuevo_apellido = input("Ingrese el nuevo apellido: ")
                contacto_actualizar['apellido'] = nuevo_apellido
                print("Apellido actualizado exitosamente.")
            case 3:
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                for contacto in contactos:  
                    if nuevo_telefono == contacto["telefono"] and contacto != contacto_actualizar: #Verifico que no exista otro contacto con el mismo teléfono
                        print("Ya existe un contacto con ese número de teléfono.")
                        return
                contacto_actualizar['telefono'] = nuevo_telefono
                print("Teléfono actualizado exitosamente.")
            case 4:
                nuevo_email = input("Ingrese el nuevo email: ")
                for contacto in contactos:  
                    if nuevo_email.lower() == contacto["email"].lower() and contacto != contacto_actualizar: #Verifico que no exista otro contacto con el mismo email
                        print("Ya existe un contacto con ese email.")
                        return
                contacto_actualizar['email'] = nuevo_email
                print("Email actualizado exitosamente.")
            case 5: 
                print("Operación cancelada.")
                return
        print("Contacto actualizado con éxito.")
        
    elif len(contactos_encontrados) > 1:
        print("Demasiados contactos encontrados. Por favor, sea más específico.")
        mostrar_contactos(contactos_encontrados)
        return
    else:
        print(f"No se encontraron contactos que coincidan con '{termino_busqueda}'")
        return  

def eliminar_contacto(contactos):
    print("--- Eliminar Contacto ---")
    termino_busqueda = input("Ingrese el nombre o apellido a eliminar: ")
    print(f"\nResultado de la busqueda para '{termino_busqueda}'")

    contactos_encontrados = []
    for contacto in contactos: # Busco todos los contactos que coincidan con el término de búsqueda
        nombre_completo = f"{contacto['nombre']} {contacto['apellido']}"
        if termino_busqueda.lower() in nombre_completo.lower():
            contactos_encontrados.append(contacto)

    if len(contactos_encontrados) == 1: 
        contacto_eliminar = contactos_encontrados[0]
        print("Contacto encontrado: ")
        mostrar_contactos(contactos_encontrados)
        confirmacion = input("¿Está seguro que desea eliminar este contacto? (s/n): ")
        if confirmacion.lower() == 's':
            contactos.remove(contacto_eliminar)
            print("Contacto eliminado exitosamente.")
        else:
            print("Operación cancelada.")
            return
    elif len(contactos_encontrados) > 1:
        print("Demasiados contactos encontrados. Por favor, sea más específico.")
        mostrar_contactos(contactos_encontrados)
        return
    else:
        print(f"No se encontraron contactos que coincidan con '{termino_busqueda}'")
        return      
