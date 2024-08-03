from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "CristhianManuel"
    edad = 29
    estatura = 1.60
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: CristhianManuel\nEdad: 29\nEstatura: 1.60\n"
