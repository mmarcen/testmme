from saludos import hola, adios

def hello_world():
    return "Hello, World!"

def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n <= 1:
        return n
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def get_user_info():
    """
    Obtiene el nombre, apellido y país del usuario.

    Returns:
        tuple: (nombre, apellido, pais) ingresados por el usuario.
    
    Raises:
        ValueError: Si alguno de los campos está vacío.
    """
    name = input("Por favor, introduce tu nombre: ")
    apellido = input("Por favor, introduce tu apellido: ")
    pais = input("Por favor, introduce tu país: ")
    if not name or not apellido or not pais:
        raise ValueError("El nombre, apellido y país no pueden estar vacíos.")
    return name, apellido, pais

if __name__ == "__main__":
    try:
        name, apellido, pais = get_user_info()
        print(hola(name, apellido, pais))
        
        # Test fibonacci
        num = int(input("Introduce un número para calcular Fibonacci: "))
        result = fibonacci(num)
        print(f"Fibonacci({num}) = {result}")
        print(adios(pais))
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
