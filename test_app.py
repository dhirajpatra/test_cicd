import app


# just a test
def test_answer():
    assert app.test_method(5) == 25


def test_zero():
    assert app.test_method(0) == 0
