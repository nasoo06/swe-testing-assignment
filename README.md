# Quick-Calc

Quick-Calc is a lightweight command-line calculator application built in Python. It supports the four basic arithmetic operations — addition, subtraction, multiplication, and division — along with a clear function that resets the calculator state. The application is designed with a clean separation between pure calculation logic and the stateful `Calculator` class, making it easy to test at multiple levels.

## Setup Instructions

**Prerequisites:** Python 3.8 or higher.

1. Clone the repository:
   ```bash
   git clone https://github.com/nasoo06/swe-testing-assignment.git
   cd swe-testing-assignment
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the test dependency:
   ```bash
   pip install pytest
   ```

4. Run the application:
   ```bash
   python calculator.py
   ```

## How to Run Tests

Execute the entire test suite (unit + integration) with a single command:

```bash
pytest -v
```

This will discover and run all test files inside the `tests/` directory.

## Testing Framework Research: Pytest vs Unittest

When choosing a testing framework for a Python project, the two most common options are **Pytest** and **Unittest** (part of the standard library). Both are mature and widely used, but they differ significantly in developer experience and flexibility.

**Unittest** is Python's built-in testing framework, modelled after Java's JUnit. It uses a class-based structure where every test must be a method inside a class that inherits from `unittest.TestCase`. Assertions rely on specific methods like `assertEqual()` and `assertTrue()`. The main advantage of Unittest is that it requires no external installation — it ships with Python. However, the class-based boilerplate makes test files more verbose, and writing parameterised tests or fixtures requires additional setup.

**Pytest** takes a different approach: tests are written as simple functions using Python's native `assert` statement. There is no need for classes or special assertion methods, which leads to shorter, more readable test code. Pytest also provides a powerful fixture system for setup and teardown, built-in parameterisation with `@pytest.mark.parametrize`, and detailed failure output that shows the exact values involved in a failed assertion. The ecosystem of plugins (e.g., `pytest-cov` for coverage, `pytest-mock` for mocking) further extends its capabilities.

For this project, **Pytest** was chosen because its minimal syntax keeps test files concise and easy to read, the `pytest.raises` context manager provides a clean way to test exceptions (important for the division-by-zero edge case), and the verbose `-v` flag produces clear, structured output. Since Quick-Calc is a small project with straightforward testing needs, Pytest's simplicity and readability make it the better fit over Unittest's heavier class-based approach.
