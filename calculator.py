def add(a, b):
    return a + b

def main():
    print("Welcome to Calculator")
    print("Operation: Add")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()