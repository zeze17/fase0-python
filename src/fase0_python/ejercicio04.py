#Dada una lista de palabras, devuelve un diccionario {palabra: cantidad}.
#Hazlo primero con for, después con comprensión

palabras = ["python", "java", "python", "c++", "java", "python"]

recurrences = {}

for palabra in palabras:
    if palabra in recurrences:
        recurrences[palabra] += 1
    else:
        recurrences[palabra] = 1

print(recurrences)

numero_letras = {}
for palabra in palabras:
    if palabra in numero_letras:
        print("palabra ya paso : "+ palabra)
    else:
        numero_letras[palabra] = len(palabra)

print(numero_letras)

palabras = ["python", "java", "python", "c++", "java", "python"]

frecuencias = {
    palabra: palabras.count(palabra)
    for palabra in set(palabras)
}

print(frecuencias)
