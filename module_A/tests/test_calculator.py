import pytest
from module_A.calculator import calculate_price

def test_positive_calculation():
    assert calculate_price(5, 100) == 500

def test_negative_quantity_error():
    with pytest.raises(ValueError):
        calculate_price(-1, 100)
