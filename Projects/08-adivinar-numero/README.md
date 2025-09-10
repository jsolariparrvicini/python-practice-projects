# Juego: Adivina el Número 🎲

Este es un juego de consola clásico escrito en Python. El programa genera un número secreto y el jugador tiene un número limitado de intentos para adivinarlo.

El proyecto fue desarrollado para practicar el uso de **estructuras de control condicionales (`if`, `elif`, `else`)** para manejar la lógica del juego y dar feedback al usuario.

---
## Características

* **Número Aleatorio:** Genera un número secreto diferente en cada partida.
* **Lógica de Adivinanza:** Compara el número del jugador con el número secreto.
* **Feedback Interactivo:** Informa al jugador si su intento fue demasiado alto, demasiado bajo o correcto.
* **Sistema de Intentos:** Limita el número de oportunidades que tiene el jugador para adivinar.

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
¡Bienvenido al juego de Adivina el Número!
Tenés 5 intentos para adivinar el número entre 1 y 100.
Intento 1. Ingresá tu número: 50
El número secreto es más alto.
Intento 2. Ingresá tu número: 75
El número secreto es más bajo.
Intento 3. Ingresá tu número: 65
¡Felicidades! ¡Adivinaste el número secreto!
```