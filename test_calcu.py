import calcu
import pytest

def test_add ():
    assert calcu.add(2,3) == 5
    
def test_mult ():
    assert calcu.mult(3,5) == 15
