# Cada string representa: "NombreProducto:PrecioUnitario:CantidadEnStock"
inventario_tienda = [
    "Manzanas:150.50:50",
    "Bananas:80.00:75",
    "Leche:210.30:30",
    "Pan:180.00:40",
    "Queso:450.75:25"
]

#Analisis de productos
print("--- ANĹISIS DEL PRODUCTO 'LECHE' ---")
producto_3, precio_3, cantidad_3 = inventario_tienda[2].split(":")
precio_3 = float(precio_3)
cantidad_3 = int(cantidad_3)
valor_total_stock_3 = precio_3*cantidad_3
print(f"Nombe: {producto_3}"), print(f"Precio: {precio_3}"), print(f"Cantidad: {cantidad_3}")
print(f"Valor del stock: ${valor_total_stock_3:.2f}")

#Compartiva de productos
producto_1, precio_1, cantida_1 = inventario_tienda[0].split(":")  
producto_2, precio_2, cantida_2 = inventario_tienda[1].split(":")
precio_1 = float(precio_1)
precio_2 = float(precio_2)
mas_caro = (precio_1 >= precio_2 and producto_1) or  producto_2 #Uso los operadores lógicos como operadores cortocircuitados
precio_mayor =(precio_1 >= precio_2 and precio_1) or precio_2
print(f"\nEl producto más caro entre {producto_1} y {producto_2} es: {mas_caro}, con un precio de ${precio_mayor}")

#Reporte general de inventario con BUCLES
nombre_productos = []
valor_total_inventario = 0
cantidad_total_inventario = 0
for producto in inventario_tienda:
    nombre, precio, stock = producto.split(":")
    valor_total_inventario += float(precio)*int(stock)
    cantidad_total_inventario += int(stock)
    nombre_productos.append(nombre)

print(f"\n--- REPORTE DE INVENTARIO ---")
print(f"Productos en inventario: {', '.join(nombre_productos)}")
print(f"Valor total del inventario: ${valor_total_inventario:.2f}")
print(f"Cantidad total de productos en stock: {cantidad_total_inventario} unidades")