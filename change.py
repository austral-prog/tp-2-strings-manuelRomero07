def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    print("ingresar gasto:")
    gasto=float(input())
    print(gasto)
    print("dinero recibido")
    dinero=int(input())
    print(dinero)
    print()
    print("vuelto")
    print()
    vuelto=dinero-gasto
    pesos=int(vuelto)
    print("pesos")
    print(pesos)
    centavos=round((vuelto-pesos)*100)
    print("centavos")
    print(centavos)
change()
