import pytest

@pytest.mark.myl
def test_sample1():
    print("Hai")
    assert "myl".__eq__("myl")

@pytest.mark.regression
def test_sample2():
    print("Helloo")
    assert 1+1 < 3

@pytest.mark.smoke
def test_sample3():
    print("welcome")
    assert 1 == 1