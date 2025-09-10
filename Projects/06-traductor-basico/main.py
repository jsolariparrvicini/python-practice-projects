# Diccionario que funciona como nuestra "base de datos" de traducciones
diccionario_traduccion = {
    "hello": "hola",
    "world": "mundo",
    "python": "python",
    "developer": "desarrollador",
    "book": "libro"
}

# Lista de palabras en inglés que queremos traducir
palabras_a_traducir = ["hello", "developer", "book", "tree"]

frase_traducida = []

#Todvia no hemos visto bucles, as que traducimos cada palabra "a mano"
frase_traducida.append(diccionario_traduccion.get(palabras_a_traducir[0],palabras_a_traducir[0]))
frase_traducida.append(diccionario_traduccion.get(palabras_a_traducir[1],palabras_a_traducir[1]))
frase_traducida.append(diccionario_traduccion.get(palabras_a_traducir[2],palabras_a_traducir[2]))
frase_traducida.append(diccionario_traduccion.get(palabras_a_traducir[3],palabras_a_traducir[3]))

print(f"Traduciendo la lista: {palabras_a_traducir}")
print(f"\nFrase traducida: {', '.join(frase_traducida)}")
