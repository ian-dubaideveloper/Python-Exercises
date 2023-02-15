class MathUtils:
    def sum_to_n(n):
        if n == 1:
            return 1
        else:
            return n + MathUtils.sum_to_n(n-1)

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * MathUtils.factorial(n-1)

    def power(x, y):
        if y == 0:
            return 1
        elif y % 2 == 0:
            return MathUtils.power(x, y/2) ** 2
        else:
            return x * MathUtils.power(x, y-1)

if __name__ == '__main__':
    n = 5
    print(f"Sum from 1 to {n}: {MathUtils.sum_to_n(n)}")
    print(f"Factorial of {n}: {MathUtils.factorial(n)}")
    x, y = 2, 3
    print(f"{x} raised to the power of {y}: {MathUtils.power(x, y)}")


    """
        In a single class, create the following methods that recursively compute:
        the sum from 1 to N.
        the factorial of n.
        x raised to the power of y.
        Call each method with starter values in the main method
        
        """