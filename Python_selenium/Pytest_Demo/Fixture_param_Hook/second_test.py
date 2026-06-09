import pytest

@pytest.mark.myl
def test_sample_1():
    print("Hai")
    assert "myl".__eq__("mylu")

@pytest.mark.regression
def test_sample_2():
    print("Helloo")
    assert 1+1 < 3

@pytest.mark.smoke 
def test_sample3():
    print("welcome")
    assert 1 == 1