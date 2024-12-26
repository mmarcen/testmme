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
    name = input("Por favor, introduce tu nombre: ")
    apellido = input("Por favor, introduce tu apellido: ")
    if not name or not apellido:
        raise ValueError("El nombre y el apellido no pueden estar vacíos.")
    return name, apellido

if __name__ == "__main__":
    try:
        name, apellido = get_user_info()
        print(hola(name, apellido))
        
        # Test fibonacci
        num = int(input("Introduce un número para calcular Fibonacci: "))
        result = fibonacci(num)
        print(f"Fibonacci({num}) = {result}")
        print(adios())
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")