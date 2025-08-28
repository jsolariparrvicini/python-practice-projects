# Reporte de Inventario de Tienda 🏪

Este es un script de consola en Python que procesa una lista de productos y genera un reporte de inventario. Cada producto en la lista de origen es un string que contiene el nombre, el precio y la cantidad en stock, separados por dos puntos.

El principal desafío de este proyecto fue realizar todos los análisis y cálculos **sin utilizar bucles ni condicionales**, aplicando únicamente conocimientos de **listas, strings y operadores**.

---
## Características

* **Análisis Detallado:** Extrae y muestra información específica de un producto, calculando el valor total de su stock.
* **Comparativa de Precios:** Compara productos y determina cuál es el más caro usando lógica de cortocircuito.
* **Reporte General:** Calcula y muestra el valor total de todo el inventario y la cantidad total de unidades en stock.

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