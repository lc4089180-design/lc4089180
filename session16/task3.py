#Given the following buggy code, fix it so that it handles division by zero and prints 'Cannot divide by zero' instead of crashing:<br><br>def calculate_discount(price, discount):<br> return price / discount<br>print(calculate_discount(1000, 0))<br><br><em><strong>Hint:</strong> Use try-except to catch ZeroDivisionError.</em>
def calculate_discount(price, discount):
    try:
        return price / discount
    except ZeroDivisionError:
        print("Cannot divide by zero")


print(calculate_discount(1000, 0))

#If you want only the required message without None, use:
def calculate_discount(price, discount):
    try:
        return price / discount
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(calculate_discount(1000, 0))