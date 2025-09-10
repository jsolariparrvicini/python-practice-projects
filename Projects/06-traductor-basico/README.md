# Traductor Básico Inglés-Español 🗣️

Este es un script de consola en Python que simula un traductor simple. Utiliza un diccionario como base de conocimiento para traducir una lista predefinida de palabras del inglés al español.

## Versiones

Este proyecto contiene dos implementaciones:

* **`main.py` (Versión 1):** Resuelve el problema de forma manual, procesando cada palabra de la lista individualmente.
* **`mainV2.py` (Versión 2):** Es una versión **refactorizada y mejorada** que utiliza un bucle `for` para iterar sobre la lista de palabras, haciendo el código más corto, limpio y escalable.

---
## Características

* **Base de Conocimiento:** Utiliza un diccionario de Python para almacenar los pares de palabras (inglés-español).
* **Traducción de Listas:** Procesa una lista de palabras y busca la traducción de cada una.
* **Manejo de Palabras Desconocidas:** Si una palabra no se encuentra en el diccionario, la añade a la frase final sin traducir, utilizando el método `.get()` para evitar errores.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3** instalado.
2.  Navega hasta el directorio del proyecto en tu terminal.
3.  Ejecuta el comando correspondiente a la versión que deseas probar:

    **Para la versión original (manual):**
    ```bash
    python main.py
    ```
    **Para la versión refactorizada (con bucle):**
    ```bash
    python mainV2.py
    ```
---
## Ejemplo de Salida

```text
Traduciendo la lista: ['hello', 'developer', 'book', 'tree']

Frase traducida: hola, desarrollador, libro, tree
```