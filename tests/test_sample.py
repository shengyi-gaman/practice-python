def test_truth():
    assert True


def test_basic_math():
    """Test basic mathematical operations"""
    # Addition
    assert 2 + 3 == 5    
    assert 10 + 0 == 10
    assert -5 + 5 == 0
    
    # Subtraction
    assert 10 - 3 == 7
    assert 5 - 5 == 0
    assert 0 - 3 == -3
    
    # Multiplication
    assert 4 * 3 == 12
    assert 7 * 0 == 0
    assert -2 * 3 == -6
    
    # Division
    assert 15 / 3 == 5
    assert 8 / 2 == 4
    assert 7 / 2 == 3.5
    
    # Modulo
    assert 10 % 3 == 1
    assert 15 % 5 == 0
    assert 7 % 2 == 1
    
    # Exponentiation
    assert 2 ** 3 == 8
    assert 5 ** 2 == 25
    assert 3 ** 0 == 1
