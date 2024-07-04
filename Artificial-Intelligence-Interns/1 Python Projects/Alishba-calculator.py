print("====CALCULATOR====")
# Function to add two numbers
def add(x, y):
    a =  x + y
    return a

# Function to subtract two numbers
def subtract(x, y):
    a = x - y
    return a

# Function to multiply two numbers
def multiply(x, y):
    a =  x * y
    return a

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "sorry it cannot be divided, please enter another option"
    a = x / y
    return a

# Main calculator loop
while True:
    print("please choose a Option:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input("Enter your option: ")

    if user_input == "quit":
        break

    if user_input in ("add", "subtract", "multiply", "divide"):
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        if user_input == "add":
            print("The addition of two numbers is: ", add(num_1, num_2))
        elif user_input == "subtract":
            print("The subtraction of two numbers is: ", subtract(num_1, num_2))
        elif user_input == "multiply":
            print("The multiplication of two numbers is: ", multiply(num_1, num_2))
        elif user_input == "divide":
            print("The division of two numbers is: ", divide(num_1, num_2))
    else:
        print("Invalid input")