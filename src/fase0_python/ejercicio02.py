#Recibe un string y devuelve: invertido, en mayúsculas,
# número de vocales. Usa slicing (texto[::-1])

def analizar_texto(texto):
    invertido = texto[::-1]
    mayusculas = texto.upper()
    vocales = "aeiouáéíóú"
    cantidad_vocales = 0

    for letra in texto.lower():
        if letra in vocales:
            cantidad_vocales += 1

    return invertido, mayusculas, cantidad_vocales

texto = "Hola Mundo"
print(analizar_texto(texto))



