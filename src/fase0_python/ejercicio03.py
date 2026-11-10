#FizzBuzz del 1 al 30. Luego una función es_primo(n)
# con valor por defecto y type hints

# ==========================================
# 1. FIZZBUZZ DEL 1 AL 30
# ==========================================

for i in range(1, 31):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)


# ==========================================
# 2. FUNCION PARA SABER SI UN NUMERO ES PRIMO
# ==========================================

def es_primo(n: int = 7) -> bool:

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


# ==========================================
# 3. EJEMPLOS DE USO
# ==========================================

print("\n===== NUMEROS PRIMOS =====")

print(es_primo())       # True (valor por defecto: 7)
print(es_primo(2))      # True
print(es_primo(9))      # False
print(es_primo(13))     # True
print(es_primo(20))     # False
