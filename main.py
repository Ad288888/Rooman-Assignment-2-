def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, **")
    
    try:
        x = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %, **): ")
        y = float(input("Enter second number: "))
        
        result = {
            '+': x + y,
            '-': x - y,
            '*': x * y,
            '/': x / y if y != 0 else "Cannot divide by zero",
            '%': x % y if y != 0 else "Cannot divide by zero",
            '**': x ** y
        }.get(op, "Invalid operator")
        
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
