def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    print("Welcome to Calculator")
    print("Operations: 1. Add  2. Subtract  3. Multiply")
    op = input("Choose operation (1-3): ")
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
        else:
            print("Error: Invalid operation")
            return
        print(f"Result: {num1} {op_symbol} {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()