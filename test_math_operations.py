# test_math_operations.py
import pytest
from math_operations import divide, reverse_string

# --- Test Cases for divide() ---
def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0

def test_divide_negative_numbers():
    assert divide(-10, -2) == 5.0
    assert divide(-10, 2) == -5.0

def test_divide_by_zero():
    # Pytest assertion to check if a specific exception is raised
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# --- Test Cases for reverse_string() ---
def test_reverse_normal_string():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    assert reverse_string("") == ""

def test_reverse_invalid_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(12345)