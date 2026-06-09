import pytest_check as check
import pytest

@pytest.mark.order()
def test_soft():
    check.assert_equal(1,2)
    assert 1 == 2
    print("Not working")

def test_soft1():
    print("1. work")
    check.equal(1,7)
    print("2. Work")
    check.equal("myl","my")