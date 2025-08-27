texto_a_analizar = input("Ingrese un texto: ").rstrip()
letras = input("Ingrese 3 letras separadas por coma: ").lower()
print(letras)

a,b,c,d,e = letras #De acá nos interesan a, c y e (las otras contienen a las comas)
#La mejor forma de hacerlo sería con split(",") pero lo hacemos así para practicar desempaquetado

cant_palabras_texto = len(texto_a_analizar.split())
# python_en_texto = ("Python" in texto_a_analizar ) or ("python" in texto_a_analizar) Hay una forma más eficiente de hacerlo:
python_en_texto = "python" in texto_a_analizar.lower()

print("\n--- ANĹISIS DEL TEXTO ---")
print(f"La letra '{a}' aparce {texto_a_analizar.count(a)} veces")
print(f"La letra '{c}' aparce {texto_a_analizar.count(c)} veces")
print(f"La letra '{e}' aparce {texto_a_analizar.count(e)} veces")
print(f"El texto tiene {cant_palabras_texto} palabras")
print(f"La primera letra del texto es '{texto_a_analizar[0]}' y la última '{texto_a_analizar[-1]}'")
print(f"El texto invertido es: {texto_a_analizar[::-1]}")
print(f"El texto 'Python' se encuentra en la cadena: {python_en_texto}")