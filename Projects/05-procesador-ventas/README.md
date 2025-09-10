# Mini Procesador de Datos de Ventas 📊

Este script de consola en Python procesa una lista de registros de ventas para generar un reporte consolidado. Cada registro de venta es un string con un formato específico ("ID,Categoría,Monto").

Este fue un proyecto integrador diseñado para combinar y aplicar los conocimientos de todas las estructuras de datos fundamentales de Python (strings, listas, tuplas, sets, diccionarios) bajo la restricción de no utilizar bucles ni condicionales.

---
## Características

* **Limpieza de Datos:** Corrige formatos de datos incorrectos en los registros de entrada.
* **Procesamiento y Estructuración:** Parsea los strings de ventas y los convierte en una lista de tuplas para un manejo más robusto.
* **Análisis de Datos:** Calcula métricas clave como el total de ventas y extrae información única como las categorías de productos.
* **Generación de Reportes:** Consolida toda la información analizada en un diccionario final.

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
Ventas procesadas (primeras 3): [('101', 'Electrónica', 1200.5), ('102', 'Libros', 150.75), ('103', 'Ropa', 300.2)]
Categorías únicas (primeras 3): {'Ropa', 'Electrónica', 'Libros'}

--- Reporte Final de Ventas ---
{'total_ventas': 1651.45, 'categorias_unicas': {'Electrónica', 'Libros', 'Ropa'}, 'primeras_tres_ventas': [('101', 'Electrónica', 1200.5), ('102', 'Libros', 150.75), ('103', 'Ropa', 300.2)]}
```