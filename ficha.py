def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre = input()
    nombre_limpio = nombre.strip().title()
    Email = input()
    Email_limpio = Email.lower()
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    Caracteres_en_nombre = len(nombre_limpio)
    espacio = nombre_limpio.find(" ")
    Iniciales = nombre_limpio[0] + nombre_limpio[espacio + 1]
    apellido = nombre_limpio[espacio + 1:]
    nombre_ap = nombre_limpio[:espacio]
    usuario = apellido + "." + nombre_ap
    usuario_lower = usuario.lower()
    Email_valido = "@" in Email_limpio
    pos_arroba = Email_limpio.find("@")
    dominio = Email_limpio[pos_arroba + 1:]
    nombreguion = nombre_limpio.replace(" ", "_")
    nombre_a = nombre_limpio.lower().count("a")
    codigo_secreto = nombre_limpio[::-1].upper()
    suma = n1 + n2 + n3
    promedio = suma / 3
    promedio_entero = suma // 3
    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {Email_limpio}")
    print(f"Caracteres en nombre: {Caracteres_en_nombre}")
    print(f"Iniciales: {Iniciales}")
    print(f"Usuario: {usuario_lower}")
    print(f"Email valido: {Email_valido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombreguion}")
    print(f"Cantidad de a: {nombre_a}")
    print(f"Codigo secreto: {codigo_secreto}")
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)


ficha()