# Gestor de Tareas Interactivo ✔️

Este es un script de consola en Python que funciona como una lista de tareas pendientes (To-Do list). El usuario puede agregar nuevas tareas, marcar tareas como completadas y eliminarlas.

Este proyecto fue un desafío para practicar la manipulación avanzada de **listas** y **strings**, e implementar lógica condicional sin el uso de sentencias `if`.

---
## Características

* **Ver Tareas:** Muestra la lista actual de tareas pendientes.
* **Agregar Tarea:** Permite añadir una nueva tarea, evitando que se agreguen duplicados.
* **Marcar como Completada:** Modifica una tarea existente para marcarla como finalizada (ej: `[X] Estudiar Python`).
* **Eliminar Tarea:** Borra una tarea de la lista.

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
--- GESTOR DE TAREAS ---
Tareas pendientes: Enviar el reporte mensual, Revisar facturas, Llamar al cliente X

Ingrese una nueva tarea: Estudiar Python
Tarea agregada.

Ingrese el nombre exacto de la tarea completada: Enviar el reporte mensual
['[X] Enviar el reporte mensual', 'Revisar facturas', 'Llamar al cliente X', 'Estudiar Python']

Ingrese el nombre exacto de la tarea a eliminar: Revisar facturas
['[X] Enviar el reporte mensual', 'Llamar al cliente X', 'Estudiar Python']

Quedan 3 pendientes
```