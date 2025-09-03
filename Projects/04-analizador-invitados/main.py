# Usamos sets para las listas de invitados, ya que no puede haber duplicados
invitados_tech = {"Ana", "Juan", "Pedro", "Maria", "Luis"}
invitados_gaming = {"Carlos", "Maria", "Luis", "Ana", "Sofia"}

invitados_totales = invitados_gaming | invitados_tech
invitados_ambos_eventos = invitados_gaming & invitados_tech
invitados_solo_tech = invitados_tech - invitados_gaming


print("--- ANÁLISIS DE LISTA DE INVITADOS ---")
print(f"Todos los invitados (sin duplicados): {', '.join(invitados_totales)}")
print(f"Invitados que asisten a ambos eventos: {', '.join(invitados_ambos_eventos)}")
print(f"Invitados que solo van al evento de Tech: {', '.join(invitados_solo_tech)}")

print("\n--- VRIFICACIÓN DE ASISTENCIA ---")
invitado_verifiacado = input("Ingrese el nombre de un invitado para verificar: ")

presente_en_lista = invitado_verifiacado.capitalize() in invitados_totales
mensajes = [f"{invitado_verifiacado} NO está en la lista.", f"Confirmado: {invitado_verifiacado} está en la lista!"]
print(mensajes[presente_en_lista])
