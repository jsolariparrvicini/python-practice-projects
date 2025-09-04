# Analizador de Listas de Invitados 🗣️

Este es un script de consola en Python que utiliza la estructura de datos `set` para gestionar y analizar dos listas de invitados a eventos.

El proyecto fue diseñado para practicar las operaciones de conjuntos (unión, intersección, diferencia) en un escenario práctico, demostrando la eficiencia de los sets para manejar colecciones de elementos únicos.

---
## Características

* **Análisis de Asistencia:** Determina la lista completa de invitados únicos, los que asisten a ambos eventos y los que asisten a un único evento.
* **Eficiencia:** Utiliza los operadores de conjuntos (`|`, `&`, `-`) para realizar los análisis de forma rápida y concisa.
* **Verificación de Invitados:** Permite al usuario consultar si una persona específica se encuentra en la lista general de invitados.

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
--- ANÁLISIS DE LISTAS DE INVITADOS ---

Todos los invitados (sin duplicados): ['Ana', 'Carlos', 'Juan', 'Luis', 'Maria', 'Pedro', 'Sofia']

Invitados que asisten a ambos eventos: ['Ana', 'Luis', 'Maria']

Invitados que solo van al evento de Tech: ['Juan', 'Pedro']

--- VERIFICACIÓN DE ASISTENCIA ---
Ingrese el nombre de un invitado para verificar: Pedro
¡Confirmado! Pedro está en la lista de invitados.
```