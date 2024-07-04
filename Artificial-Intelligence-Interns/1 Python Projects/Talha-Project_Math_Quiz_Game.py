import random

marks = 0

# Dictionary for operators and their symbols
operators = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply',
    '/': 'divide',
    '%': 'find the remainder when dividing',
}

for _ in range(10):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(list(operators.keys()))
    operation = operators[operator]

    print(f"Question: What is the answer when you {operation} {num1} and {num2}?")

    answer = eval(f"{num1} {operator} {num2}")
    options = [answer, random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)]
    random.shuffle(options)

    options_dict = {chr(97 + i): options[i] for i in range(4)}
    correct_choice = [key for key, value in options_dict.items() if value == answer][0]

    for key, value in options_dict.items():
        print(f"{key}) {value}")

    choice = input("Enter your choice: ").lower()

    if choice == correct_choice:
        marks += 4
        print("Your answer is correct, Your Marks:", marks, "\n")
    else:
        marks -= 1
        print(f"Your answer is wrong, Your Marks: {marks}")
        print(f"The answer is ({correct_choice}) {answer}\n")

print("Total marks:", marks)