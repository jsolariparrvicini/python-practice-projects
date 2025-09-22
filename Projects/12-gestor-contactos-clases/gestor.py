import os
import json

class Contacto:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nombre} {self.apellido} | Tel: {self.telefono} | Email: {self.email}"



class GestorContactos:
    def __init__(self,archivo = "contactos.json"):
        self.contactos = []
        self.archivo = archivo
        self.cargar_contactos()
    
    def cargar_contactos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo,"r") as file:
                data = json.load(file) #Json.load devuelve una lista de diccionarios
                self.contactos = [Contacto(**c) for c in data] #Por cada diccionario en data, crea una instancia de Contacto usando los valores del diccionario. EL ** desempaqueta el diccionario en argumentos de palabra clave.

    def guardar_contactos(self):
        with open(self.archivo,"w") as file:
            json.dump([c.__dict__ for c in self.contactos],file, indent=4) #Convierte cada instancia de Contacto en un diccionario usando __dict__ y guarda la lista de diccionarios en el archivo JSON. Indent=4 para que el JSON sea legible.
    
    def mostrar_contactos(self,lista_contactos = None):
        contactos_a_mostrar = lista_contactos if lista_contactos is not None else self.contactos
        if not contactos_a_mostrar:
            print("No hay contactos para mostrar.")
            return
        print("----------------")
        for index,contacto in enumerate(contactos_a_mostrar):
            print(f"{index + 1}. {contacto}")
        print("----------------")

    def agregar_contacto(self,nuevo_contacto):
        for contacto in self.contactos:
            if nuevo_contacto.telefono == contacto.telefono:
                print("\nYa existe un contacto con ese número de teléfono. No se puede agregar el contacto.")
                return
            elif nuevo_contacto.email.lower() == contacto.email.lower():
                print("\nYa existe un contacto con ese email. No se puede agregar el contacto.")
                return
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nuevo_contacto.nombre} {nuevo_contacto.apellido}' agregado exitosamente.")

    def buscar_contacto(self,termino_busqueda):
        contactos_encontrados = []
        for contacto in self.contactos:
            nombre_completo = f"{contacto.nombre} {contacto.apellido}"
            if termino_busqueda.lower() in nombre_completo.lower():
                contactos_encontrados.append(contacto)
        return contactos_encontrados

    def eliminar_contacto(self,contacto):
        self.contactos.remove(contacto)
        print(f"Contacto '{contacto.nombre} {contacto.apellido}' eliminado exitosamente.")


    def actualizar_contacto(self,contacto,campo,nuevo_valor):
        if campo in ["telefono","email"]:
            for c in self.contactos:
                if nuevo_valor == getattr(c,campo) and c != contacto: #Verifico que no exista otro contacto con el mismo teléfono o email.
                    print(f"Ya existe un contacto con ese {campo}. No se puede actualizar.")
                    return 
        setattr(contacto,campo,nuevo_valor)
        print(f"{campo.capitalize()} actualizado exitosamente.")

    def seleccionar_contacto(self, termino):
        resultados = self.buscar_contacto(termino)
        if not resultados:
            print("No se encontraron contactos.")
            return None
        if len(resultados) > 1:
            print("Demasiados contactos. Sea más específico.")
            self.mostrar_contactos(resultados)
            return None
        return resultados[0]
