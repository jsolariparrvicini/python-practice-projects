# Validador de Fortaleza de Contraseña 🔐

Este es un script de consola en Python que analiza una contraseña introducida por el usuario para verificar si cumple con un conjunto de criterios de seguridad estándar.

El proyecto fue un desafío avanzado para integrar y aplicar conocimientos de **strings, listas, sets, condicionales y operadores lógicos**, bajo la restricción de **no utilizar bucles**.

---
## Criterios de Validación

El script verifica los siguientes cinco criterios de fortaleza:

1.  **Longitud Mínima:** La contraseña debe tener al menos 8 caracteres.
2.  **Mayúsculas:** Debe contener al menos una letra mayúscula.
3.  **Minúsculas:** Debe contener al menos una letra minúscula.
4.  **Números:** Debe contener al menos un dígito numérico.
5.  **Símbolos Especiales:** Debe contener al menos un símbolo de la lista `!@#$%^&*()-_=+[]{}|;:,.<>/?~`.

Se considera que una contraseña es **segura** si cumple con **3 o más** de estos requisitos.

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
Ingrese su contraseña para validar su fortaleza: ClaveSegura#1
Analizando...

--- REPORTE DE FORTALEZA ---
[X] La contraseña tiene al menos 8 caracteres.
[X] La contraseña contiene al menos una mayúscula.
[X] La contraseña contiene al menos una minúscula.
[X] La contraseña contiene al menos un número.
[X] La contraseña contiene al menos un carácter especial.

La contraseña es segura
```