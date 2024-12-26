from main import * 
from saludos import hola, adios
from main import hello_world
import pytest

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_hola():
    assert hola("Juan", "Perez") == "Hola, Juan Perez"

def test_adios():
    assert adios() == "Bye"
    
def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_regular():
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

@pytest.mark.parametrize("n,expected", [
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (8, 21),
    (10, 55)
])
def test_fibonacci_parametrized(n, expected):
    assert fibonacci(n) == expected

def test_fibonacci_negative():
    with pytest.raises(ValueError, match="El número debe ser positivo"):
        fibonacci(-1)

def test_fibonacci_non_integer():
    """
    Test the fibonacci function with non-integer inputs.

    This test ensures that the fibonacci function raises a TypeError
    when provided with inputs that are not integers. Specifically, it
    checks for the following cases:
    - A floating-point number (3.14)
    - A string ("5")

    The expected error message is "El número debe ser un entero".
    """
    with pytest.raises(TypeError, match="El número debe ser un entero"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="El número debe ser un entero"):
        fibonacci("5")