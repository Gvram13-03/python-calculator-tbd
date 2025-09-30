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

def main():
    while True:
        print("\nWelcome to Calculator")
        print("Operations: 1. Add  2. Subtract  3. Multiply  4. Divide  5. Quit")
        op = input("Choose operation (1-5): ")
        if op == "5":
            print("Goodbye!")
            break
        if op not in ["1", "2", "3", "4"]:
            print("Error: Invalid operation")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if op == "1":
                result = add(num1, num2)
                op_symbol = "+"
            elif op == "2":
                result = subtract(num1, num2)
                op_symbol = "-"
            elif op == "3":
                result = multiply(num1, num2)
                op_symbol = "*"
            elif op == "4":
                result = divide(num1, num2)
                op_symbol = "/"
            print(f"Result: {num1} {op_symbol} {num2} = {result}")
        except ValueError:
            print("Error: Please enter valid numbers")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()