# Juego: Adivina el Número 🎲

Este es un juego de consola clásico escrito en Python. El programa genera un número secreto y el jugador tiene un número limitado de intentos para adivinarlo.

## Versiones

Este proyecto contiene dos implementaciones:

* **`main.py` (V1):** La versión inicial, desarrollada para practicar el uso de **estructuras de control condicionales (`if`, `elif`, `else`)** de forma repetitiva.
* **`mainV2.py` (V2):** La versión definitiva, **refactorizada con un bucle `while`**. Esta versión es más eficiente, escalable y demuestra una estructura de código profesional.

---
## Características

* **Número Aleatorio:** Genera un número secreto diferente en cada partida.
* **Bucle de Juego (V2):** Un bucle `while` controla el flujo del juego, permitiendo múltiples intentos de forma automática.
* **Feedback Interactivo:** Informa al jugador si su intento fue demasiado alto, demasiado bajo o correcto.
* **Sistema de Intentos:** Limita el número de oportunidades y finaliza el juego si el jugador se queda sin intentos.
* **Salida Limpia:** El uso de `break` y la cláusula `while...else` aseguran que el juego termine correctamente tanto en caso de victoria como de derrota.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3** instalado.
2.  Navega hasta el directorio del proyecto en tu terminal.
3.  Ejecuta el comando correspondiente a la versión que deseas probar:

    **Para la versión original (sin bucles):**
    ```bash
    python main.py
    ```
    **Para la versión definitiva (con bucles):**
    ```bash
    python mainV2.py
    ```
---
## Ejemplo de Interacción

**Escenario de Victoria:**
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

**Escenario de Derrota:**
```text
¡Bienvenido al juego de Adivina el Número!
Tenés 5 intentos para adivinar el número entre 1 y 100.
...
Intento 5. Ingresá tu número: 80
El número secreto es más bajo.

Se te terminaron los intentos, no lo adivinaste.
El número secreto era 72
```