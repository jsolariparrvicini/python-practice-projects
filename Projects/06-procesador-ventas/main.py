# main.py
# Cada string representa: "ID_Producto,Categoría,MontoVenta"
ventas_raw = [
    "101,Electrónica,1200,50",
    "102,Libros,150.75",
    "103,Ropa,300.20",
    "101,Electrónica,1350.00", # Venta repetida del mismo producto
    "104,Hogar,550.45",
    "102,Libros,175.50"
]
# Corregir el primer registro que tiene un error en el monto (debe ser 1200.50)
registro_a_corregir = ventas_raw[0]
ventas_raw[0] = registro_a_corregir[::-1].replace(",",".",1)[::-1] # Corregimos el primer registro  

#Procesamiento de ventas
#Se puede mejorar mucho este código usando bucles y funciones, pero aún no hemos visto esos conceptos.
primera_venta = ventas_raw[0].split(",")
primera_venta[-1] = float(primera_venta[-1]) # Convertimos el monto a float
primera_venta = tuple(primera_venta) # Convertimos la lista a tupla

segunda_venta = ventas_raw[1].split(",")
segunda_venta[-1] = float(segunda_venta[-1]) # Convertimos el monto a float
segunda_venta = tuple(segunda_venta) # Convertimos la lista a tupla

tercera_venta = ventas_raw[2].split(",")
tercera_venta[-1] = float(tercera_venta[-1]) # Convertimos el monto a float
tercera_venta = tuple(tercera_venta) # Convertimos la lista a tupla
 
ventas = [primera_venta, segunda_venta, tercera_venta]

print(f"Ventas procesadas (primeras 3): {ventas}")

#Análisis de categorias
categorias_unicas = set()
categorias_unicas.add(primera_venta[1])
categorias_unicas.add(segunda_venta[1])
categorias_unicas.add(tercera_venta[1])
print(f"Categorías únicas (primeras 3): {categorias_unicas}")

#Reporte final
total_ventas = primera_venta[-1] + segunda_venta[-1] + tercera_venta[-1]

reporte_venta = {}
reporte_venta["total_ventas"] = total_ventas
reporte_venta["categorias_unicas"] = categorias_unicas
reporte_venta["primeras_tres_ventas"] = ventas

print("\n--- Reporte Final de Ventas ---")
print(reporte_venta)



