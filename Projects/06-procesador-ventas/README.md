# Mini Procesador de Datos de Ventas 📊

Este es un script de consola en Python que procesa una lista de registros de ventas para generar un reporte consolidado. Cada registro de venta es un string con un formato específico ("ID,Categoría,Monto").

## Versiones

Este proyecto contiene dos implementaciones:

* **`main.py` (Versión 1):** Resuelve el desafío aplicando únicamente conocimientos de estructuras de datos, **sin utilizar bucles**. Procesa solo los tres primeros registros de forma manual.
* **`mainV2.py` (Versión 2):** Es una versión **refactorizada y mejorada** que utiliza un bucle `for` para procesar la lista completa de ventas de forma automática y escalable, demostrando una solución más profesional.

---
## Características

* **Limpieza de Datos:** Corrige formatos de datos incorrectos en los registros de entrada.
* **Procesamiento y Estructuración:** Parsea los strings de ventas y los convierte en una lista de tuplas.
* **Análisis de Datos:** Calcula métricas clave como el total de ventas y extrae las categorías únicas de productos.
* **Generación de Reportes:** Consolida toda la información analizada en un diccionario final.

---
## Cómo Ejecutarlo

1.  Asegúrate de tener **Python 3** instalado.
2.  Navega hasta el directorio del proyecto en tu terminal.
3.  Ejecuta el comando correspondiente a la versión que deseas probar:

    **Para la versión original (sin bucles):**
    ```bash
    python main.py
    ```
    **Para la versión refactorizada (con bucles):**
    ```bash
    python mainV2.py
    ```
---
## Ejemplo de Salida (Versión V2)

La salida del `mainV2.py` (que procesa todos los datos) es la siguiente:

```text
Ventas procesadas: [('101', 'Electrónica', 1200.5), ('102', 'Libros', 150.75), ('103', 'Ropa', 300.2), ('101', 'Electrónica', 1350.0), ('104', 'Hogar', 550.45), ('102', 'Libros', 175.5)]
Categorías únicas: {'Hogar', 'Ropa', 'Electrónica', 'Libros'}

--- Reporte Final de Ventas ---
{'total_ventas': 3727.4, 'categorias_unicas': {'Hogar', 'Ropa', 'Electrónica', 'Libros'}, 'ventas': [('101', 'Electrónica', 1200.5), ('102', 'Libros', 150.75), ('103', 'Ropa', 300.2), ('101', 'Electrónica', 1350.0), ('104', 'Hogar', 550.45), ('102', 'Libros', 175.5)]}
```