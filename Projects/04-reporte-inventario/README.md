# Reporte de Inventario de Tienda 🏪

Este es un script de consola en Python que procesa una lista de productos y genera un reporte de inventario. Cada producto en la lista de origen es un string que contiene el nombre, el precio y la cantidad en stock, separados por dos puntos.

## Versiones

Este proyecto contiene dos versiones:

* **`main.py` (Versión 1):** Resuelve el problema aplicando únicamente conocimientos de listas, strings y operadores, **sin utilizar bucles**.
* **`mainV2.py` (Versión 2):** Es una versión **refactorizada y mejorada** que utiliza un bucle `for` para procesar el inventario de forma automática y escalable, demostrando una solución más profesional y eficiente.

---
## Características

* **Análisis Detallado:** Extrae y muestra información específica de un producto, calculando el valor total de su stock.
* **Comparativa de Precios:** Compara productos y determina cuál es el más caro.
* **Reporte General:** Calcula y muestra el valor total de todo el inventario y la cantidad total de unidades en stock.

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
## Ejemplo de Salida
```text
--- ANÁLISIS DEL PRODUCTO 'LECHE' ---
Nombre: Leche
Precio: 210.30
Cantidad: 30
Valor del stock: $6309.00

El producto más caro entre Manzanas y Bananas es: Manzanas, con un precio de $150.5

--- REPORTE DE INVENTARIO ---
Productos en inventario: Manzanas, Bananas, Leche, Pan, Queso
Valor total del inventario: $29916.25
Cantidad total de productos en stock: 220 unidades
```