"""Simple command-line calculator."""

import argparse


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main(argv=None):
    """Entry point for the command-line interface."""
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div"],
        help="Operation to perform",
    )
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")
    args = parser.parse_args(argv)

    operations = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
    }

    result = operations[args.operation](args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
