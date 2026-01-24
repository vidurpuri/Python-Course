a_input = input("Enter first number: ")
b_input = input("Enter second number: ")

while True:
    try:
        a = int(a_input)
        b = int(b_input)
        print(f"Adding {a} + {b} = {a + b}")
        break
    except ValueError:
        print("Invalid input: please enter integer values.")
        a_input = input("Enter first number: ")
        b_input = input("Enter second number: ")
    except Exception as e:
        print(f"Error occurred: {e}")
        break