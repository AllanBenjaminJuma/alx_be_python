class Calculator:
    """
    A class demonstrating the use of static methods and class methods.
    """
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It does not require access to instance or class-specific data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        It uses the 'cls' parameter to access a class attribute.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b