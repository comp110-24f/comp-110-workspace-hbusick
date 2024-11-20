"""11/18 Class on Recursive structures"""


def factorial(n: int) -> int:
    """Compute the factorial of n."""
    # base case
    if n == 0 or n == 1:
        return 1
    else:
        # recursive case
        return n * factorial(n - 1)


print(factorial(3))
