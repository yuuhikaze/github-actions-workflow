from app.calculator import sum, sub

def test_sum() -> None:
    assert sum(2,3) == 5

def test_sub() -> None:
    # premeditated failure
    assert sub(5,3) == 1
