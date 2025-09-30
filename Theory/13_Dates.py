## Dates ##

from datetime import datetime 

now = datetime.now() #Instancia objeto con fecha y hora actual

print(now) #Fecha y hora actual
print(now.year)
print(now.month)
print(now.day)  
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp() #Convierte la fecha y hora a un número de punto flotante que representa los segundos desde el 1 de enero de 1970
print(timestamp)            # Sirve como representacion única de un momento en el tiempo para almacenamiento o comparación

dt_from_timestamp = datetime.fromtimestamp(timestamp) #Convierte el timestamp de vuelta a un objeto datetime
print(dt_from_timestamp) #Sirve para recuperar la fecha y hora original desde el timestamp

dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #Convierte el objeto datetime a una cadena formateada
print(dt_string) #Sirve para mostrar la fecha y hora en un formato legible o específico

# Crear un objeto datetime específico
dt_specific = datetime(2026, 1, 1)
print(dt_specific) 

# Crear un objeto datetime a partir de una cadena
dt_from_string = datetime.strptime("01/01/2026", "%d/%m/%Y") #Sirve para analizar una cadena (ej extraída de un archivo o entrada del usuario) y convertirla en un objeto datetime
print(dt_from_string)

from datetime import time 
# Crear un objeto time específico. La diferencia con datetime es que time solo maneja horas, minutos, segundos y microsegundos, sin información de fecha.
# Sirve para representar un momento específico del día sin asociarlo a una fecha concreta.
# Por ejemplo, para horarios de apertura, alarmas, etc.
t = time(14, 30, 0) #14:30:00
print(t)
print(t.hour)

# Crear un objeto time a partir de una cadena
t_from_string = time.fromisoformat("14:30:00") #Sirve para analizar una cadena (ej extraída de un archivo o entrada del usuario) y convertirla en un objeto time
print(t_from_string)

# Crear un time a partir de un datetime
t_from_dt = now.time() #Extrae la parte de tiempo de un objeto datetime
print(t_from_dt)


from datetime import date
# Crear un objeto date específico. La diferencia con datetime es que date solo maneja año, mes y día, sin información de tiempo.
# Sirve para representar una fecha específica sin asociarla a una hora concreta.
# Por ejemplo, para fechas de cumpleaños, aniversarios, etc.
d = date(2023, 12, 25) #25 de diciembre de 2023
print(d) 
print(d.year)

d_now = date.today() #Obtiene la fecha actual sin la hora
print(d_now)

# Crear un objeto date a partir de una cadena
d_from_string = date.fromisoformat("2023-12-25") #Sirve para analizar una cadena (ej extraída de un archivo o entrada del usuario) y convertirla en un objeto date
print(d_from_string)

# Crear un date a partir de un datetime
d_from_dt = now.date() #Extrae la parte de fecha de un objeto datetime
print(d_from_dt)

from datetime import timedelta
# Crear un objeto timedelta que representa una duración de tiempo
# Diferencia entre dos fechas
dt1 = datetime(2023, 1, 1)
dt2 = datetime(2024, 1, 1)
delta = dt2 - dt1 #Resta dos objetos datetime para obtener un objeto timedelta que representa la diferencia entre las dos fechas
print(delta) #Sirve para calcular la duración entre dos fechas, útil para medir plazos, edades, etc.

# Crear un timedelta específico
td = timedelta(days=10, hours=5, minutes=30) #10 días, 5 horas, 30 minutos
print(td) #Sirve para representar una duración específica que se puede sumar o restar a objetos datetime
# Sumar un timedelta a un datetime
new_dt = now + td #Suma un objeto timedelta a un objeto datetime para obtener una nueva fecha y hora
print(new_dt) #Sirve para calcular fechas futuras o pasadas basadas en una duración específica
