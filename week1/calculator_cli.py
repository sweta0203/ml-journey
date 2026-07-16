# creating functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a**b


while True:
    operation = input("\nChoose (+, -, *, /, ** or 'quit'): ").strip()

    if operation.lower() == "quit":
        print("Goodbye!")
        break

    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if operation == "+":
            print("Result:", add(num1, num2))

        elif operation == "-":
            print("Result:", subtract(num1, num2))

        elif operation == "*":
            print("Result:", multiply(num1, num2))

        elif operation == "/":
            print("Result:", divide(num1, num2))

        elif operation == "**":
            print("Result:", power(num1, num2))

        else:
            print("Invalid operation.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Please enter valid numbers.")
