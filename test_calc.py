from calc import add
def test_add_working():
    assert add(2,3) == 5
def test_add_not_working():
    assert add(2,3) == 6