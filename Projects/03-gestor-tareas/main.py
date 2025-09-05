
# La lista de tareas será una lista de strings.
tareas = ["Enviar el reporte mensual", "Revisar facturas", "Llamar al cliente X"]

#Tareas iniciales
print("--- GESTOR DE TAREAS ---")
print(f"Treas pendientes: {', '.join(tareas)}")

#Agregado de treas
nueva_tarea = input("Ingrese una nueva tarea: ")
ya_existe = nueva_tarea in tareas 

(not ya_existe) and tareas.append(nueva_tarea) #Si la tarea no existe, la agrega a la lista. El and y el or son operadores cortocircuitados.
mensajes = ["Tarea agregada.", "La tarea ya existe."]
print(mensajes[ya_existe]) #Uso el valor de verdad como índice

# print(tareas)

#Marcar una tarea completada
tarea_completada = input("\nIngrese el nombre exacto de la tarea completada: ")
index_tarea_completada = tareas.index(tarea_completada)
tareas[index_tarea_completada] = f"[x] {tarea_completada}" #Los f strings no solo van con el print
print(tareas)

#Eliminar una tarea
tarea_a_eliminar = input("\nIngrese el nombre exacto de la tarea a eliminar: ")
tareas.remove(tarea_a_eliminar)
print(tareas)

#Resumen final
print(f"Quedan {len(tareas)} pendientes")

"""
Lecciones aprendidas:
- Usar el and y el or como operadores cortocircuitados para evitar un if
- Usar el valor de verdad como índice de una lista
- Usar f strings para formatear strings
"""