#
#   Write a program that given two numbers as input make the main operations.
#
#   Output:
#   Insert first number: 4
#   Insert second number: 2
#
#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2
#
"""Simple calculator performing the four main operations on two numbers."""

from typing import Optional


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """Return the quotient of a and b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def read_number(prompt: str) -> float:
    """Ask the user for a number until a valid one is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again.")


def format_number(value: float) -> str:
    """Format a number without useless trailing decimals (2.0 -> 2)."""
    return f"{value:g}"


def main() -> None:
    """Read two numbers and print the results of the main operations."""
    first = read_number("Insert first number: ")
    second = read_number("Insert second number: ")

    print()
    print(f"SUM: {format_number(add(first, second))}")
    print(f"Difference: {format_number(subtract(first, second))}")
    print(f"Multiplication: {format_number(multiply(first, second))}")

    quotient = divide(first, second)
    if quotient is None:
        print("Division: impossible (division by zero)")
    else:
        print(f"Division: {format_number(quotient)}")


if __name__ == "__main__":
    main()
