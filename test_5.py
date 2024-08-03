from programa import area_circulo

def test_suma():
    assert area_circulo(2, 3) == 5
    assert area_circulo(-1, 5) == 4
