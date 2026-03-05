"""
Quick-Calc: A simple command-line calculator application.
Supports addition, subtraction, multiplication, division, and clear.
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """A stateful calculator that tracks the current result and supports chained operations."""

    def __init__(self):
        self.result = 0.0
        self._pending_operator = None
        self._pending_operand = None

    def clear(self):
        """Reset the calculator state to zero."""
        self.result = 0.0
        self._pending_operator = None
        self._pending_operand = None

    def enter_number(self, value: float):
        """Set the current operand."""
        self._pending_operand = value

    def set_operator(self, operator: str):
        """Store the operator and move the current operand into result."""
        if self._pending_operand is not None:
            if self._pending_operator is not None:
                self._evaluate()
            else:
                self.result = self._pending_operand
        self._pending_operator = operator
        self._pending_operand = None

    def equals(self) -> float:
        """Evaluate the pending operation and return the result."""
        if self._pending_operator is not None and self._pending_operand is not None:
            self._evaluate()
        elif self._pending_operand is not None:
            self.result = self._pending_operand
        self._pending_operator = None
        self._pending_operand = None
        return self.result

    def _evaluate(self):
        """Perform the pending arithmetic operation."""
        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }
        if self._pending_operator in operations:
            self.result = operations[self._pending_operator](self.result, self._pending_operand)

    def get_display(self) -> str:
        """Return the current display value as a formatted string."""
        if self._pending_operand is not None:
            value = self._pending_operand
        else:
            value = self.result
        if value == int(value):
            return str(int(value))
        return str(value)


def main():
    """Run the interactive command-line calculator."""
    calc = Calculator()
    print("Quick-Calc — Type 'q' to quit, 'c' to clear")
    print("Enter expressions as: number operator number =")
    print("Example: 5 + 3 =\n")

    while True:
        user_input = input(">> ").strip().lower()

        if user_input == "q":
            print("Goodbye!")
            break
        elif user_input == "c":
            calc.clear()
            print("Cleared. Display: 0")
            continue

        tokens = user_input.split()
        try:
            i = 0
            while i < len(tokens):
                token = tokens[i]
                if token == "=":
                    result = calc.equals()
                    display = calc.get_display()
                    print(f"= {display}")
                elif token in ("+", "-", "*", "/"):
                    calc.set_operator(token)
                else:
                    calc.enter_number(float(token))
                i += 1
        except ValueError as e:
            print(f"Error: {e}")
            calc.clear()
        except Exception as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
