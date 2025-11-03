from feladatok import egyedi_betuk

def test_egyedi_betuk():
    assert egyedi_betuk("Hello, Világ!") == ['a', 'e', 'g', 'h', 'i', 'l', 'o', 'v']
    assert egyedi_betuk("Python 3.12") == ['h', 'n', 'o', 'p', 't', 'y']
    assert egyedi_betuk("Árvíztűrő tükörfúrógép") == ['a', 'e', 'f', 'g', 'k', 'o', 'p', 'r', 't', 'u', 'v', 'z']
    assert egyedi_betuk("") == []
    print("Minden teszt lefutott")


test_egyedi_betuk()
