def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input()
    apellido = input()

    completo = nombre + " " + apellido

    print(completo.lower())
    print(completo.title())
    print(completo.upper())
    print("\t" + completo.lower())
