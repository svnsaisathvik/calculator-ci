import pytest
from app import add, sub, mul, div

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(5,2) == 3

def test_mul():
    assert mul(4,2) == 8

def test_div():
    assert div(10,2) == 5

def test_div_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        div(3,0)
