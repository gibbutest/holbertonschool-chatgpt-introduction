#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n. If n is 0, returns 1.

    Raises:
        RecursionError: If n is too large for recursion.
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Ensure a command-line argument was provided
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        result = factorial(number)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
