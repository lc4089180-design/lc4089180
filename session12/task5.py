#Refactor the following code by moving the repeated logic into a function named is_even, which returns True if a number is even and False otherwise. Then, use this function to print all even numbers from 1 to 20.<br><br><em><strong>Hint:</strong> Use the modulus operator (%) to check for even numbers.</em>
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


for number in range(1, 21):
    if is_even(number):
        print(number)