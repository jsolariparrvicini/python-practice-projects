# Wordle de Consola 🔡

Este es un clon del popular juego de adivinanzas "Wordle", desarrollado para ser jugado en la línea de comandos. El proyecto fue creado como un desafío integrador para aplicar todos los fundamentos de Python aprendidos.

El juego demuestra un manejo avanzado de **bucles, condicionales, estructuras de datos y manipulación de strings** para crear una experiencia de juego interactiva y completa.

---
## Características

* **Palabra Secreta Aleatoria:** Elige una palabra al azar de una lista predefinida en cada partida.
* **Bucle de Juego Controlado:** Un bucle `for` gestiona los 6 intentos permitidos.
* **Validación de Entrada:** Un bucle `while` anidado asegura que el usuario solo ingrese palabras de 5 letras alfabéticas.
* **Feedback Visual con Colores:** Utiliza códigos de color de la consola para indicar el estado de cada letra:
    * **Verde:** Letra correcta en la posición correcta.
    * **Amarillo:** Letra correcta en la posición incorrecta.
    * **Gris:** Letra incorrecta.
* **Manejo de Victoria y Derrota:** El juego termina si el jugador adivina la palabra o se queda sin intentos, mostrando el mensaje correspondiente.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3** instalado.
2.  Navega hasta el directorio del proyecto en tu terminal.
3.  Ejecuta el siguiente comando:

    ```bash
    python main.py
    ```
---
## Ejemplo de Interacción

```text
¡Bienvenido a Wordle de Consola!
Intento 1/6: Ingresa una palabra de 5 letras: GATOS
Feedback: 🟨 ⬜ ⬜ 🟨 ⬜

Intento 2/6: Ingresa una palabra de 5 letras: JUEGO
¡Felicidades! ¡Adivinaste la palabra secreta: JUEGO!
```