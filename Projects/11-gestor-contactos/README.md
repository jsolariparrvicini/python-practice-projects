# Gestor de Contactos de Consola 📔

Este es un script de consola en Python que funciona como una aplicación completa para la gestión de contactos. Permite al usuario realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) sobre una lista de contactos.

El proyecto es una demostración integral de los fundamentos de Python, incluyendo el manejo de estructuras de datos (listas, diccionarios), el control de flujo (bucles y condicionales), la organización del código en funciones y la persistencia de datos a través de archivos de texto.

---
## Características

* **Persistencia de Datos:** Los contactos se cargan desde un archivo `contactos.txt` al iniciar el programa y se guardan automáticamente al salir.
* **Gestión de Contactos (CRUD):**
    * **Ver:** Muestra una lista formateada de todos los contactos.
    * **Buscar:** Permite buscar contactos por nombre o apellido (búsqueda parcial e insensible a mayúsculas).
    * **Agregar:** Añade nuevos contactos a la lista, validando para evitar teléfonos o emails duplicados.
    * **Actualizar:** Permite modificar un contacto existente tras una búsqueda específica.
    * **Eliminar:** Borra un contacto de la lista, previa confirmación del usuario.
* **Menú Interactivo:** Un menú principal claro y fácil de usar que guía al usuario a través de las diferentes opciones.
* **Manejo de Errores:** Valida la entrada del usuario para asegurar que las opciones del menú sean correctas y maneja errores de formato.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3** instalado.
2.  Clona o descarga el repositorio.
3.  Navega hasta el directorio del proyecto en tu terminal.
4.  Ejecuta el siguiente comando:

    ```bash
    python main.py
    ```
    La primera vez que se ejecute, se creará automáticamente un archivo `contactos.txt` si no existe.

---
## Ejemplo de Interacción

```text
--- GESTOR DE CONTACTOS ---
1. Ver lista de contactos
2. Buscar contacto
3. Agregar nuevo contacto
4. Actualizar contacto
5. Eliminar contacto
6. Salir

Seleccione una opción: 1

--- LISTA DE CONTACTOS ---
----------------
1. Nombre: Juan Perez, Teléfono: 555-8888, Email: juan.perez@email.com
2. Nombre: Ana Garcia, Teléfono: 555-1234, Email: ana.garcia@email.com
----------------
```