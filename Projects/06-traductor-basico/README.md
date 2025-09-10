# Traductor Básico Inglés-Español 🗣️

Este es un script de consola en Python que simula un traductor simple. Utiliza un diccionario como base de conocimiento para traducir una lista predefinida de palabras del inglés al español.

El proyecto fue diseñado para practicar el uso de **diccionarios** como una estructura de datos para búsquedas rápidas (clave-valor) y el manejo de casos donde una clave no existe.

---
## Características

* **Base de Conocimiento:** Utiliza un diccionario de Python para almacenar los pares de palabras (inglés-español).
* **Traducción de Listas:** Procesa una lista de palabras y busca la traducción de cada una.
* **Manejo de Palabras Desconocidas:** Si una palabra no se encuentra en el diccionario, la añade a la frase final sin traducir, evitando errores. Se utiliza el método `.get()` para lograr esto de forma eficiente.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3** instalado.
2.  Navega hasta el directorio del proyecto en tu terminal.
3.  Ejecuta el siguiente comando:

    ```bash
    python main.py
    ```

---
## Ejemplo de Salida

```text
Traduciendo la lista: ['hello', 'developer', 'book', 'tree']

Frase traducida: hola, desarrollador, libro, tree
```