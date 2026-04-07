class Calculator:
    """Simple calculator with validation"""

    @staticmethod
    def add(a, b):
        Calculator._validate_numbers(a, b)
        return a + b

    @staticmethod
    def subtract(a, b):
        Calculator._validate_numbers(a, b)
        return a - b

    @staticmethod
    def multiply(a, b):
        Calculator._validate_numbers(a, b)
        return a * b

    @staticmethod
    def divide(a, b):
        Calculator._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def _validate_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")