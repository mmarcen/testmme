from saludos import hola, adios

def hello_world():
    return "Hello, World!"

def get_user_info():
    name = input("Por favor, introduce tu nombre: ")
    apellido = input("Por favor, introduce tu apellido: ")
    if not name or not apellido:
        raise ValueError("El nombre y el apellido no pueden estar vacíos.")
    return name, apellido

if __name__ == "__main__":
    print(adios())
    try:
        name, apellido = get_user_info()
        print(hola(name, apellido))
    except ValueError as e:
        print(f"Error: {e}")

        