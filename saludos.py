def hola(nombre, apellido, pais):
    """
    Devuelve un saludo personalizado en el idioma local del país.

    Args:
        nombre (str): El nombre de la persona.
        apellido (str): El apellido de la persona.
        pais (str): El país de la persona.

    Returns:
        str: Un saludo personalizado en el idioma correspondiente.
    """
    saludos = {
        "España": f"¡Hola, {nombre} {apellido}!",
        "Francia": f"Bonjour, {nombre} {apellido}!",
        "Italia": f"Ciao, {nombre} {apellido}!",
        "Alemania": f"Hallo, {nombre} {apellido}!",
        "Inglaterra": f"Hello, {nombre} {apellido}!",
        "Portugal": f"Olá, {nombre} {apellido}!",
        "Japón": f"こんにちは, {nombre} {apellido}!",
        "China": f"你好, {nombre} {apellido}!",
        "Brasil": f"Oi, {nombre} {apellido}!"
    }
    
    return saludos.get(pais, f"Hola, {nombre} {apellido}")  # Si el país no está en el diccionario, saluda en español

def adios():
    """
    Devuelve una despedida.

    Returns:
        str: Una despedida.
    """
    return "adios"
