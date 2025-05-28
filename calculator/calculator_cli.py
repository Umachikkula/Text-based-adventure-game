from calculator.logger import log_operation
from calculator.db_handler import save_to_db

def calculator():
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator (+ - * /): ")
            b = float(input("Enter second number: "))

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    print("Error: Division by zero.")
                    continue
                result = a / b
            else:
                print("Invalid operator.")
                continue

            print("Result:", result)
            log_operation(a, op, b, result)
            save_to_db(a, op, b, result)

        except ValueError:
            print("Invalid input.")

        if input("Continue? (y/n): ").lower() != 'y':
            break
