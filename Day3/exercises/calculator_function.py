def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


def test_calculator():
    # Test cases
    test_cases = [
        {"function": add, "inputs": (3, 5), "expected": 8},
        {"function": add, "inputs": (-2, -3), "expected": -5},
        {"function": subtract, "inputs": (10, 4), "expected": 6},
        {"function": subtract, "inputs": (5, 8), "expected": -3},
        {"function": multiply, "inputs": (4, 7), "expected": 28},
        {"function": multiply, "inputs": (0, 10), "expected": 0},
        {"function": divide, "inputs": (10, 2), "expected": 5},
        {"function": divide, "inputs": (5, 0), "expected": "Cannot divide by zero"},
    ]

    # Testing each case
    for i, case in enumerate(test_cases):
        func = case["function"]
        inputs = case["inputs"]
        expected = case["expected"]

        # Call the function with the inputs
        result = func(*inputs)

        # Check if the result matches the expected value
        if result == expected:
            print(f"Test case {i + 1} passed: {func.__name__}{inputs} = {result}")
        else:
            print(f"Test case {i + 1} failed: {func.__name__}{inputs} = {result}, expected {expected}")

# Run the tests
test_calculator()
