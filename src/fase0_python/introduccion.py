
# =====================================================
# INTRODUCCION A PYTHON
# Ejemplos básicos de la documentación oficial
# =====================================================


# 1. OPERACIONES MATEMATICAS
print("\n===== 1. OPERACIONES MATEMATICAS =====")

print(5 + 3)    # Suma: 8
print(5 - 3)    # Resta: 2
print(5 * 3)    # Multiplicacion: 15
print(5 / 2)    # Division: 2.5
print(5 // 2)   # Division entera: 2
print(5 % 2)    # Modulo: 1
print(5 ** 2)   # Potencia: 25


# 2. VARIABLES Y TIPOS NUMERICOS
print("\n===== 2. VARIABLES =====")

edad = 20        # int
altura = 1.75    # float

print(edad)
print(altura)

ancho = 20
alto = 5
resultado = ancho * alto

print("Area:", resultado)


# 3. CADENAS DE TEXTO (STRINGS)
print("\n===== 3. STRINGS =====")

nombre = "Sergio"
apellido = "Herrera"

print("Hola " + nombre)
print(nombre * 3)
print("Hola\nMundo")

texto = "Python"

print("Longitud:", len(texto))


# 4. ACCEDER A CARACTERES
print("\n===== 4. INDICES =====")

palabra = "Python"

print(palabra[0])    # P
print(palabra[1])    # y
print(palabra[-1])   # n


# 5. SLICING (SEGMENTACION)
print("\n===== 5. SLICING =====")

palabra = "Python"

print(palabra[0:2])  # Py
print(palabra[2:5])  # tho
print(palabra[:2])   # Py
print(palabra[2:])   # thon


# 6. LISTAS
print("\n===== 6. LISTAS =====")

numeros = [10, 20, 30, 40, 50]

print(numeros)
print(numeros[0])
print(numeros[-1])


# 7. MODIFICAR ELEMENTOS DE UNA LISTA
print("\n===== 7. MODIFICAR LISTAS =====")

numeros = [10, 20, 30]

numeros[0] = 100

print(numeros)


# 8. AGREGAR ELEMENTOS
print("\n===== 8. APPEND =====")

numeros = [10, 20, 30]

numeros.append(40)

print(numeros)


# 9. CONCATENAR LISTAS
print("\n===== 9. CONCATENAR LISTAS =====")

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = lista1 + lista2

print(resultado)


# 10. LISTAS ANIDADAS (MATRICES)
print("\n===== 10. MATRICES =====")

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz[0][1])  # 2


# 11. OPERADORES DE COMPARACION
print("\n===== 11. COMPARACIONES =====")

a = 10
b = 5

print(a < b)    # Menor que
print(a > b)    # Mayor que
print(a == b)   # Igual que
print(a <= b)   # Menor o igual
print(a >= b)   # Mayor o igual
print(a != b)   # Diferente


# 12. CONDICIONALES
print("\n===== 12. CONDICIONALES =====")

edad = 20

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# 13. CICLO WHILE
print("\n===== 13. CICLO WHILE =====")

contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1


# 14. SUCESION DE FIBONACCI
print("\n===== 14. FIBONACCI =====")

a, b = 0, 1

while a < 100:
    print(a)
    a, b = b, a + b


# 15. FUNCIONES IMPORTANTES
print("\n===== 15. FUNCIONES =====")

numeros = [10, 20, 30, 40, 50]

print("Longitud:", len(numeros))
print("Redondeo:", round(3.14159, 2))

