import pytest

@pytest.mark.xfail(reason="Just skip")
def test_sample1():
    print("Hai")
    assert "myl".__eq__("my ")
 
@pytest.mark.xfail(reason="Just skip")
def test_sample2():
    print("Helloo")
    assert 1+1 < 3  

@pytest.mark.parametrize("a1,a2",[(1,2),(1,2),(1,2)])
def test_sample3(a1,a2):
    assert a1 +2 == a2