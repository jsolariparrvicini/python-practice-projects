# Mini Analizador de Texto 📝

Este proyecto es un script de consola creado en Python que realiza un análisis básico de un texto introducido por el usuario. Fue desarrollado como parte de un roadmap de aprendizaje de Python, utilizando principalmente los conceptos aprendidos en el manejo de strings.

---
## Características

* **Conteo de Letras:** Cuenta la frecuencia de 3 letras específicas (elegidas por el usuario) dentro del texto.
* **Conteo de Palabras:** Calcula el número total de palabras en el texto.
* **Letras Clave:** Muestra cuál es la primera y la última letra del texto.
* **Texto Invertido:** Presenta una versión del texto original escrito al revés.
* **Búsqueda de Palabra:** Verifica si la palabra "Python" se encuentra en el texto.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3** instalado.
2.  Clona o descarga este repositorio y navega hasta la carpeta del proyecto.
3.  Ejecuta el siguiente comando en tu terminal:

    ```bash
    python main.py
    ```

---
## Ejemplo de Uso

La interacción con el programa se ve de la siguiente manera:

```text
Ingrese un texto: Python es un lenguaje de programación increíble
Ingrese 3 letras separadas por coma: p,e,n

--- ANÁLISIS DEL TEXTO ---
La letra 'p' aparce 2 veces
La letra 'e' aparce 5 veces
La letra 'n' aparce 4 veces
El texto tiene 7 palabras
La primera letra del texto es 'P' y la última 'e'
El texto invertido es: elbercni nóicamargorp ed ejaugnel nu se nohtyP
El texto 'Python' se encuentra en la cadena: True
```
Conteo de palabras: ¿Cuántas palabras hay en total en todo el texto? (Pista: investiga el método .split()).

Letra de inicio y fin: ¿Cuál es la primera y la última letra del texto? (Usa indexación).

Texto invertido: Muestra el texto completo pero en orden inverso. (Usa slicing).

Búsqueda de la palabra "Python": Imprime True si la palabra "Python" se encuentra en el texto y False si no está. (Pista: usa el operador in).

Ejemplo de Interacción:

Ingresa un texto: Python es un lenguaje de programación increíble
Ingresa 3 letras separadas por coma: p,e,n

--- ANÁLISIS DEL TEXTO ---
La letra 'p' aparece 2 veces.
La letra 'e' aparece 5 veces.
La letra 'n' aparece 4 veces.
El texto tiene 7 palabras.
La primera letra es 'P' y la última es 'e'.
El texto invertido es: elbercni nóicamargorp ed ejaugnel nu se nohtyP
La palabra 'Python' sí se encuentra en el texto.