# my_project/example.py

class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    # Numpy style
    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The sum of the two numbers.
        """
        return a + b

    # docstring Google style 예시
    def add2(a, b):
        """Compute and return the sum of two numbers.

        Args:
            a (float): A number representing the first addend in the addition.
            b (float): A number representing the second addend in the addition.

        Returns:
            float: A number representing the arithmetic sum of `a` and `b`.


        Examples:
            >>> add(4.0, 2.0)
            6.0
            >>> add(4, 2)
            6.0

        """

        return float(a + b)
