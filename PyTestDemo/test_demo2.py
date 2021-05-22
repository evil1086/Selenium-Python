import pytest


def test_firstprogramme():
    msg = "hello"
    assert msg == "hi", "String doesnt match the values"


@pytest.mark.smoke
# To skip the marker from the execution
@pytest.mark.skip
def test_creditcard():
    a = 2
    b = 4
    assert a+b == 6, "Calculation doesnt match"
