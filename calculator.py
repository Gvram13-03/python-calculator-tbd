def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def main():
    history = []
    enable_power = True  # Feature flag for exponentiation
    while True:
        print("\nWelcome to Calculator")
        ops_menu = "Operations: 1. Add  2. Subtract  3. Multiply  4. Divide  5. Show History"
        if enable_power:
            ops_menu += "  6. Power"
        ops_menu += "  7. Quit"
        print(ops_menu)
        op = input("Choose operation (1-7): ").strip()
        if op == "7":
            print("Goodbye!")
            break
        if op == "5":
            if history:
                print("\nCalculation History:")
                for calc in history:
                    print(calc)
            else:
                print("No calculations yet")
            continue
        if enable_power and op == "6":
            op_choice = "6"
        elif op in ["1", "2", "3", "4"]:
            op_choice = op
        else:
            print("Error: Invalid operation, choose 1-7")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if op_choice == "1":
                result = add(num1, num2)
                op_symbol = "+"
            elif op_choice == "2":
                result = subtract(num1, num2)
                op_symbol = "-"
            elif op_choice == "3":
                result = multiply(num1, num2)
                op_symbol = "*"
            elif op_choice == "4":
                result = divide(num1, num2)
                op_symbol = "/"
            elif op_choice == "6" and enable_power:
                result = power(num1, num2)
                op_symbol = "^"
            calc = f"{num1} {op_symbol} {num2} = {result}"
            history.append(calc)
            print(f"Result: {calc}")
        except ValueError:
            print("Error: Please enter valid numbers")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()