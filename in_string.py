def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre=input("Introduce un nombre: ").lower()
    print("a" in nombre)
    print("e" in nombre)
    print("i" in nombre)
    print("o" in nombre)
    print("u" in nombre)

