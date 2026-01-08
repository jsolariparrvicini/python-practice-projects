#main.py
from datetime import datetime, timedelta
print("--- CALCULADORA DE PLAZOS DE PROYECTO ---")

inicio_str = input("Ingrese la fecha y hora de inicio (dd/mm/aaaa HH:MM): ")
finalizacion_str = input("Ingrese la fecha y hora de finalización (dd/mm/aaaa HH:MM): ")
try:
    inicio = datetime.strptime(inicio_str,"%d/%m/%Y %H:%M")
    finalizacion = datetime.strptime(finalizacion_str,"%d/%m/%Y %H:%M")
except ValueError:
    print("\n Error: Formato de fecha y hora incorrecto. Use dd/mm/aaaa HH:MM")
    exit(1)

duracion = finalizacion - inicio
if duracion < timedelta(0):
    print("\n Error: La fecha de finalización debe ser posterior a la fecha de inicio.")
    exit(1)

print(duracion)
print("-\n-- ANÁLISIS DEL CRONOGRAMA ---")



