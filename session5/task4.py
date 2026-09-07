#Build a script that takes a user's name as input and prints a welcome message 5 times using a for loop with range().<br><br><em><strong>Hint:</strong> Use input() to get the name and range(5) in your loop.</em>
name = input("Enter your name: ")

for i in range(5):
    print(f"Welcome, {name}!")