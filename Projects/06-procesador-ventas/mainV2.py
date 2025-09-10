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
total_ventas = 0.0
ventas = []
categorias_unicas = set()
for venta_raw in ventas_raw:
    venta = venta_raw.split(",")
    venta[-1] = float(venta[-1])
    venta = tuple(venta)
    ventas.append(venta) #Creo lista de ventas
#Aprovechamos el bucle para obtener las categorias unicas
    categorias_unicas.add(venta[1])
#Obtenemos el total de ventas
    total_ventas += venta[-1]

print(f"Ventas procesadas: {ventas}")
print(f"Categorías únicas: {categorias_unicas}")

reporte_venta = {}
reporte_venta["total_ventas"] = round(total_ventas,3)
reporte_venta["categorias_unicas"] = categorias_unicas
reporte_venta["ventas"] = ventas

print("\n--- Reporte Final de Ventas ---")
print(reporte_venta)





