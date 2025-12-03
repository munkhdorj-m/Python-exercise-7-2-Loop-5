import pytest
import inspect
from assignment import (
    average_of_digits,
    product_smallest_largest,
    count_digits_divisible_by_3,
    reverse_number
)

def uses_loop(func):
    source = inspect.getsource(func)
    return "for" in source or "while" in source


# --- Exercise 1: Average of digits ---
@pytest.mark.parametrize("num, expected", [
    (583, (5 + 8 + 3) / 3),
    (100, (1 + 0 + 0) / 3),
    (7, 7.0),
    (9999, 9.0),
])
def test1(num, expected):
    assert abs(average_of_digits(num) - expected) < 0.0001
    assert uses_loop(average_of_digits)


# --- Exercise 2: Product of smallest & largest digit ---
@pytest.mark.parametrize("num, expected", [
    (3498, 3 * 9),
    (5012, 0 * 5),
    (777, 7 * 7),
    (9182, 1 * 9),
])
def test2(num, expected):
    assert product_smallest_largest(num) == expected
    assert uses_loop(product_smallest_largest)


# --- Exercise 3: Count digits divisible by 3 ---
@pytest.mark.parametrize("num, expected", [
    (6391, 3),      # 6,3,9
    (123456, 2),    # 3,6
    (999, 3),       # all divisible
    (12486, 1),      # 6 only
    (55555, 0),     # all are 5 
])
def test3(num, expected):
    assert count_digits_divisible_by_3(num) == expected
    assert uses_loop(count_digits_divisible_by_3)


# --- Exercise 4: Reverse number ---
@pytest.mark.parametrize("num, expected", [
    (12345, 54321),
    (907, 709),
    (5, 5),
    (1000, 1),  
])
def test4(num, expected):
    assert reverse_number(num) == expected
    assert uses_loop(reverse_number)
