from main import * 
from saludos import hola, adios
from main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_hola():
    assert hola("Juan", "Perez") == "Hola, Juan Perez"

def test_adios():
    assert adios() == "adios"