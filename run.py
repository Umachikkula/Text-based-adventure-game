def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose operation (1-5): ")

        if choice == "5":
            print("Exiting Calculator.")
            break

        a = input("Enter first number: ")
        b = input("Enter second number: ")

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            print(f"Result: {a + b}")
        elif choice == "2":
            print(f"Result: {a - b}")
        elif choice == "3":
            print(f"Result: {a * b}")
        elif choice == "4":
            if b != 0:
                print(f"Result: {a / b}")
            else:
                print("Error: Division by zero.")
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    calculator()
