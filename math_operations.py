# math_operations.py

def divide(a, b):
    """Divides two numbers, raising an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def reverse_string(text):
    """Reverses the provided string."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]