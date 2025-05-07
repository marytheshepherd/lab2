from calculate import calculations


def test_calculations_odd():
    numbers = [5, 1, 3]
    avg, min_val, max_val, median = calculations(numbers.copy())
    assert avg == 3
    assert min_val == 1
    assert max_val == 5
    assert median == 3

def test_calculations_even():
    numbers = [10, 2, 4, 6]
    avg, min_val, max_val, median = calculations(numbers.copy())
    assert avg == 5.5
    assert min_val == 2
    assert max_val == 10
    assert median == 5.0
