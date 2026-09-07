#Create a simple password attempt system like Paytm: Allow the user up to 3 tries to enter the correct password using a while loop. Print 'Access Denied' if all attempts fail, or 'Welcome' if the correct password is entered.
correct_password = "1234"
attempts = 0

while attempts < 3:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Welcome")
        break

    attempts += 1
else:
    print("Access Denied")