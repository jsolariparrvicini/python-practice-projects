#main.py
contraseña = input("Ingrese su contraseña para validar su fortaleza: ")
print("Analizando...")

longitud_minima = 8
numeros = {'0','1','2','3','4','5','6','7','8','9'}
caracteres_especiales = {'!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':',',','.','<','>','/','?','|','~','`'}

cumple_longitud = len(contraseña) >= 8 
contiene_mayuscula = not (contraseña.lower() == contraseña)
contiene_minuscula = not (contraseña.upper() == contraseña)
contiene_numero = len(numeros & set(contraseña)) > 0 #Uso de sets para verificar si hay números en la contraseña. 
contiene_especiales = len(caracteres_especiales & set(contraseña)) > 0 #Uso de sets para verificar si hay caracteres especiales en la contraseña.

print("\n--- Reporte de Fortaleza ---")

print(f"{'[x]' if cumple_longitud else '[ ]'} La contraseña tiene al menos 8 caracteres.")
print(f"{'[x]'if contiene_mayuscula else '[ ]'} La contraseña contiene al menos una letra mayúscula.")
print(f"{'[x]' if contiene_minuscula else '[ ]'} La contraseña contiene al menos una letra minúscula.")
print(f"{'[x]' if contiene_numero else '[ ]'} La contraseña contiene al menos un número.")
print(f"{'[x]'if contiene_especiales else '[ ]'} La contraseña contiene al menos un carácter especial.")

cant_requisitos_cumplidos = cumple_longitud + contiene_mayuscula + contiene_minuscula + contiene_numero + contiene_especiales

if cant_requisitos_cumplidos >= 3:
    print("\nLa contraseña es segura") 
else: 
    print("\nLa contraseña es debil")