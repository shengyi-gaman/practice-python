def add(a, b):
    return a + b

def test_add_fails_intentionally():
    assert add(2, 3) == 5
    
def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(5, 3) == 2

if __name__ == "__main__":
    # Run this file's tests directly: `python fail.py`
    import sys
    import pytest

    sys.exit(pytest.main([__file__]))


