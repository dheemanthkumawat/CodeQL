#!/usr/bin/env python3
"""
simple_eval_demo.py

Demonstrates a vulnerable use of eval() on user input.
"""

def calculate_expression(expr: str) -> float:
    """
    VERY DANGEROUS: This blindly hands whatever `expr` contains to Python's eval().
    If an attacker controls `expr`, they can execute arbitrary code.
    """
    return eval(expr)


if __name__ == "__main__":
    user_input = input("Enter a Python expression (e.g. 2 + 2): ")
    try:
        result = calculate_expression(user_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error evaluating expression: {e}")
