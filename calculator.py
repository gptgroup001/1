"""Simple calculator implemented as a Flask web app."""

from flask import Flask, jsonify, request

app = Flask(__name__)


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



def _parse_args():
    """Parse `a` and `b` from request arguments."""
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a is None or b is None:
        raise ValueError("Parameters 'a' and 'b' must be numbers")
    return a, b


@app.route("/add")
def add_route():
    """Handle addition."""
    try:
        a, b = _parse_args()
        result = add(a, b)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"result": result})


@app.route("/sub")
def sub_route():
    """Handle subtraction."""
    try:
        a, b = _parse_args()
        result = subtract(a, b)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"result": result})


@app.route("/mul")
def mul_route():
    """Handle multiplication."""
    try:
        a, b = _parse_args()
        result = multiply(a, b)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"result": result})


@app.route("/div")
def div_route():
    """Handle division."""
    try:
        a, b = _parse_args()
        result = divide(a, b)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
