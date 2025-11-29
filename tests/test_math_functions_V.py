
# function to test
def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

# -------------------------
# TESTS
# -------------------------

def test_multiply():
    # correct assertion:
    # assert multiply(4, 3) == 12

    # Intentional failure to trigger CI
    assert multiply(4, 3) == 14 

def test_add():
    assert add(4, 3) == 9