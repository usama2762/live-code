import main as m
# def capital_case(x):
#     return x.capitalize()

def test_capital_case():
    assert m.capital_case('semaphore') == 'Semaphore'

def test_capital_case():
    assert m.get_max([1, 6, 3, 5]) == 6