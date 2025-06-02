# simple_eval_demo.py

def calculate_expression(expr: str) -> float:
    return eval(expr)  # ← CodeQL will flag this every time

if __name__ == "__main__":
    user_input = input("Enter a Python expression: ")
    print(calculate_expression(user_input))
