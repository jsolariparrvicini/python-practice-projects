print( "Bienvenido a la calculadora de propinas")

total_cuenta = float(input("Ingrese el monto total de la cuenta: "))
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar? (ej: 15, 18, 20): "))

monto_propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + monto_propina

print( "\n---Resumen de la cuenta ---")
print(f"Total de la cuenta: ${total_cuenta:.2f}")
print(f"Propina({porcentaje_propina}%): ${monto_propina:.2f}")
print(f"Total a pagar: ${total_con_propina:.2f}")