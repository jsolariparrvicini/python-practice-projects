# Gestor de Contactos con POO 📔

Este es un script de consola en Python que funciona como una aplicación completa para la gestión de contactos, desarrollado siguiendo los principios de la Programación Orientada a Objetos (POO).

El proyecto sirve como una demostración integral de los fundamentos de Python, incluyendo un diseño modular, manejo de estructuras de datos complejas, control de flujo, organización en clases y persistencia de datos a través de archivos JSON.

---
## Arquitectura

El proyecto está dividido en dos módulos principales para una clara separación de responsabilidades:

* **`gestor.py` (Lógica de Negocio):** Contiene las clases `Contacto` (el modelo de datos) y `GestorContactos` (el motor que maneja toda la lógica de negocio, como agregar, buscar, eliminar, guardar y cargar contactos). Este módulo no interactúa con el usuario.
* **`main.py` (Interfaz de Usuario):** Contiene el bucle principal de la aplicación, el menú y toda la lógica de interacción con el usuario (`print` e `input`). Importa y utiliza una instancia de `GestorContactos` para ejecutar las operaciones.

---
## Características

* **Persistencia de Datos con JSON:** Los contactos se cargan desde `contactos.json` al iniciar y se guardan automáticamente al salir.
* **Gestión de Contactos (CRUD):** Implementación completa de las operaciones Crear, Leer (Ver/Buscar), Actualizar y Eliminar.
* **Diseño Orientado a Objetos:** La lógica está encapsulada en clases, promoviendo la reutilización y mantenibilidad del código.
* **Validación de Datos:** Evita la creación de contactos con teléfono o email duplicados.
* **Manejo de Errores:** Valida la entrada del usuario en los menús para una experiencia de usuario robusta.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3.10** o superior (para la sintaxis `match-case`).
2.  Clona o descarga el repositorio.
3.  Navega hasta el directorio del proyecto en tu terminal.
4.  Ejecuta el siguiente comando:

    ```bash
    python main.py
    ```
    La primera vez que se ejecute, se creará automáticamente un archivo `contactos.json` si no existe.