"""Calculator app: Tkinter GUI plus a safe expression evaluator.

Run GUI:  python calculator.py
Run CLI:  python calculator.py --cli
"""
import ast
import operator
import sys

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def evaluate(expression: str):
    """Safely evaluate an arithmetic expression."""

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY:
            return UNARY[type(node.op)](_eval(node.operand))
        raise ValueError("Invalid expression")

    expression = expression.replace("×", "*").replace("÷", "/").replace("^", "**")
    try:
        result = _eval(ast.parse(expression.strip(), mode="eval"))
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero") from None
    except (SyntaxError, OverflowError, TypeError):
        raise ValueError("Invalid expression") from None
    if isinstance(result, float):
        result = round(result, 10)
        if result == int(result):
            result = int(result)
    return result


def run_gui():
    import tkinter as tk

    root = tk.Tk()
    root.title("Calculator")
    root.resizable(False, False)

    expr = tk.StringVar()
    entry = tk.Entry(root, textvariable=expr, font=("Segoe UI", 22), justify="right",
                     bd=8, relief="flat")
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=6, pady=6)
    entry.focus_set()

    def press(ch):
        expr.set(expr.get() + ch)
        entry.icursor(tk.END)

    def clear():
        expr.set("")

    def backspace():
        expr.set(expr.get()[:-1])

    def calculate(_event=None):
        try:
            expr.set(str(evaluate(expr.get())))
        except ValueError as exc:
            expr.set(str(exc))
        entry.icursor(tk.END)

    buttons = [
        ("C", clear), ("⌫", backspace), ("%", "%"), ("÷", "/"),
        ("7", "7"), ("8", "8"), ("9", "9"), ("×", "*"),
        ("4", "4"), ("5", "5"), ("6", "6"), ("-", "-"),
        ("1", "1"), ("2", "2"), ("3", "3"), ("+", "+"),
        ("0", "0"), (".", "."), ("^", "^"), ("=", calculate),
    ]
    for i, (label, action) in enumerate(buttons):
        cmd = action if callable(action) else (lambda c=action: press(c))
        tk.Button(root, text=label, font=("Segoe UI", 16), width=4, height=2,
                  command=cmd).grid(row=1 + i // 4, column=i % 4, padx=2, pady=2)

    root.bind("<Return>", calculate)
    root.bind("<Escape>", lambda _e: clear())
    root.mainloop()


def run_cli():
    print("Calculator (type 'q' to quit)")
    while True:
        line = input("> ").strip()
        if line.lower() in ("q", "quit", "exit"):
            break
        if not line:
            continue
        try:
            print(evaluate(line))
        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    run_cli() if "--cli" in sys.argv else run_gui()
