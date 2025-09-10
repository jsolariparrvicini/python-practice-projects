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
for palabra in palabras_a_traducir:
    frase_traducida.append(diccionario_traduccion.get(palabra,palabra)) # Si no está en el diccionario, dejamos la palabra original
    
print(f"Traduciendo la lista: {palabras_a_traducir}")
print(f"\nFrase traducida: {', '.join(frase_traducida)}")
