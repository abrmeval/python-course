from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_operations = {"+" : add, "-" : subtract, "*": multiply, "/": divide }

def ask_first_number():
    return float(input("What's the first number?: "))

def ask_operation():
    print("+\n-\n*\n/")
    return input("Pick an operation: ")

def ask_for_next_number():
    return float(input("What's the next number?: "))

continue_or_new = "n"
result = 0

while True:
    if continue_or_new == "y":
        first_number = result
    else:
        print("\n" * 20)
        print(logo)
        first_number = ask_first_number()

    operation = ask_operation()
    next_number = ask_for_next_number()

    math_func = math_operations[operation]
    result = math_func(first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {result}")

    continue_or_new = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ").lower()
#
# result = math_operations["*"](4, 8)
#
# print(result)