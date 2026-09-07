#Use ChatGPT or Copilot to generate a Python code snippet that reads a list of numbers from the user and prints their sum, but gracefully handles invalid (non-numeric) input using exception handling. Paste the code you got and mention which AI tool you used.
try:
    numbers = input("Enter numbers separated by spaces: ").split()

    numbers = [float(number) for number in numbers]

    print("Sum:", sum(numbers))

except ValueError:
    print("Invalid input. Please enter numbers only.")