class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return x ** 0.5