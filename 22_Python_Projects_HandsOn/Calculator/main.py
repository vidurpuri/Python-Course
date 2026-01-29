try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation.")
    print("The result is:", result)
except ValueError:
    print("Invalid input. Please enter a number.")
